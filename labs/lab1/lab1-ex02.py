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

    def add(self, name, rule):
        if name in self.rules:
            print("A rule with that name already exists. Use update instead.")
        else:
            self.rules[name] = rule
            print("Rule added.")

    def update(self, name, threshold):
        if name in self.rules:
            self.rules[name].threshold = threshold
            print("Rule updated.")
        else:
            print("Rule not found.")

    def delete(self, name):
        if name in self.rules:
            del self.rules[name]
            print("Rule deleted.")
        else:
            print("Rule not found.")

    def evaluate(self, temperature, light):
        for name, rule in self.rules.items():
            if isinstance(rule, TemperatureRule) and temperature is not None:
                result = rule.evaluate(temperature)
                print(name, ":", result)
            elif isinstance(rule, LightRule) and light is not None:
                result = rule.evaluate(light)
                print(name, ":", result)

    def rulesList(self):
        for name, rule in self.rules.items():
            if isinstance(rule, TemperatureRule):
                print(name, "- Temperature - threshold:", rule.threshold)
            elif isinstance(rule, LightRule):
                print(name, "- Light - threshold:", rule.threshold)


controller = RuleController()

while True:
    command = input("\nEnter command (add/update/delete/evaluate/rules/exit): ")
    if command == "add":
        ruleType = input("Enter rule type (temperature/light): ")
        name = input("Enter rule name: ")
        threshold = float(input("Enter threshold: "))
        if ruleType == "temperature":
            rule = TemperatureRule(threshold)
            controller.add(name, rule)
        elif ruleType == "light":
            rule = LightRule(threshold)
            controller.add(name, rule)
        else:
            print("Invalid rule type.")
    elif command == "update":
        name = input("Enter rule name: ")
        threshold = float(input("Enter new threshold: "))
        controller.update(name, threshold)
    elif command == "delete":
        name = input("Enter rule name: ")
        controller.delete(name)
    elif command == "evaluate":
        temperature = input("Enter current temperature (Enter to skip): ")
        light = input("Enter current light level (Enter to skip): ")
        if temperature != "":
            temperature = float(temperature)
        else:
            temperature = None
        if light != "":
            light = float(light)
        else:
            light = None
        controller.evaluate(temperature, light)
    elif command == "rules":
        controller.rulesList()
    elif command == "exit":
        break
    else:
        print("Invalid command.")
