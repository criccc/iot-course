"""
Develop in Object Oriented Programming (OOP) a simple “rule controller” for a Smart
Home.  Based  on  simple  rules,  the  program  should  be  able  to  manage  and  control
temperature and lights of the home.

The  program  will  display  a  menu  asking  end-user  to  insert  the  action  type  to  be
performed. The accepted commands are:
• add: to add a new rule (temperature or light)
• update: to update an existing rule
• delete: to delete an existing rule
• evaluate: to evaluate current temperature and/or light level measurement based
on the existing rules
• rules: for listing existent rules
• exit: to close the program

Hint:  You  can  start  by  creating  a  super-class  ConditionRule  with  an  attribute
threshold and a method evaluate.  Then create two sub-classes LightRule and
TemperatureRule. Finally, you can develop a class RuleController for rules
management.
"""

import cherrypy
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rulesFile = os.path.join(BASE_DIR, "rules.json")


class ConditionRule:
    def __init__(self, threshold):
        self.threshold = threshold

    def evaluate(self, value):
        return value > self.threshold


class TemperatureRule(ConditionRule):
    def evaluate(self, temperature):
        return temperature > self.threshold


class LightRule(ConditionRule):
    def evaluate(self, light):
        return light > self.threshold


class RuleController:
    def __init__(self):
        self.rules = {}

    def load_rules(self):
        self.rules = {}
        if os.path.exists(rulesFile) and os.path.getsize(self.rulesFile) > 0:
            with open(rulesFile, "r") as f:
                data = json.load(f)
                for name, info in data.items():
                    if info["type"] == "temperature":
                        self.rules[name] = TemperatureRule(info["threshold"])
                    elif info["type"] == "light":
                        self.rules[name] = LightRule(info["threshold"])

    def save_rules(self):
        data = {}
        for name, rule in self.rules.items():
            rule_type = "temperature" if isinstance(rule, TemperatureRule) else "light"
            data[name] = {"type": rule_type, "threshold": rule.threshold}
        with open(rulesFile, "w") as f:
            json.dump(data, f, indent=4)

    def get_rules_dict(self):
        self.load_rules()
        data = {}
        for name, rule in self.rules.items():
            rule_type = "temperature" if isinstance(rule, TemperatureRule) else "light"
            data[name] = {"type": rule_type, "threshold": rule.threshold}
        return {"rules_list": data}

    def add(self, name, rule_type, threshold):
        self.load_rules()
        if name in self.rules:
            raise cherrypy.HTTPError(409, "Rule already exists")

        if rule_type == "temperature":
            self.rules[name] = TemperatureRule(threshold)
        elif rule_type == "light":
            self.rules[name] = LightRule(threshold)
        else:
            raise cherrypy.HTTPError(400, "Invalid rule type")

        self.save_rules()

    def update(self, name, threshold):
        self.load_rules()
        if name not in self.rules:
            raise cherrypy.HTTPError(404, "Rule not found")

        self.rules[name].threshold = threshold
        self.save_rules()

    def delete(self, name):
        self.load_rules()
        if name not in self.rules:
            raise cherrypy.HTTPError(404, "Rule not found")

        del self.rules[name]
        self.save_rules()

    def evaluate_measurements(self, temperature, light):
        self.load_rules()
        results = {}
        for name, rule in self.rules.items():
            if isinstance(rule, TemperatureRule) and temperature is not None:
                results[name] = rule.evaluate(temperature)
            elif isinstance(rule, LightRule) and light is not None:
                results[name] = rule.evaluate(light)
        return {"evaluationResults": results}


class RuleControllerWebService:
    exposed = True

    def __init__(self):
        self.controller = RuleController()

    def GET(self, *uri):
        if len(uri) == 1 and uri[0] == "rulesList":
            try:
                return json.dumps(self.controller.get_rules_dict())
            except Exception as e:
                raise cherrypy.HTTPError(500, str(e))
        else:
            raise cherrypy.HTTPError(404, "Page not found")

    def POST(self, *uri):
        if len(uri) == 1:
            action = uri[0]
            try:
                body = cherrypy.request.body.load()
                content = json.loads(body) if body else {}
                if action == "addRule":
                    name = content.get("name")
                    rule_type = content.get("type")
                    threshold = content.get("threshold")

                    if not name or not rule_type or threshold is None:
                        raise cherrypy.HTTPError(400, "Missing parameters")

                    self.controller.add(name, rule_type, float(threshold))
                    return json.dumps(self.controller.get_rules_dict())

                elif action == "evaluate":
                    temperature = content.get("temperature")
                    light = content.get("light")

                    temp_val = float(temperature) if temperature is not None else None
                    light_val = float(light) if light is not None else None

                    results = self.controller.evaluate_measurements(temp_val, light_val)
                    return json.dumps(results)
            except Exception as e:
                raise cherrypy.HTTPError(500, str(e))
            else:
                raise cherrypy.HTTPError(404, "Page not found")

    def PUT(self, *uri):
        if len(uri) == 2 and uri[0] == "updateRule":
            rule_name = uri[1]
            try:
                body = cherrypy.request.body.read()
                content = json.loads(body)
                threshold = content.get("threshold")

                if threshold is None:
                    raise cherrypy.HTTPError(400, "Missing threshold")

                self.controller.update(rule_name, float(threshold))
                return json.dumps(self.controller.get_rules_dict())

            except Exception as e:
                if isinstance(e, cherrypy.HTTPError):
                    raise e
                raise cherrypy.HTTPError(500, f"Internal Server Error: {str(e)}")
        else:
            raise cherrypy.HTTPError(404, "Page not found")

    def DELETE(self, *uri):
        if len(uri) == 2 and uri[0] == "deleteRule":
            rule_name = uri[1]
            try:
                self.controller.delete(rule_name)
                return json.dumps(self.controller.get_rules_dict())
            except Exception as e:
                if isinstance(e, cherrypy.HTTPError):
                    raise e
                raise cherrypy.HTTPError(500, f"Internal Server Error: {str(e)}")
        else:
            raise cherrypy.HTTPError(404, "Page not found")


if __name__ == "__main__":
    conf = {"/": {"request.dispatch": cherrypy.dispatch.MethodDispatcher()}}

    cherrypy.tree.mount(RuleControllerWebService(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
