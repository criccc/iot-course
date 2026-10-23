import cherrypy
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
devicesFile = os.path.join(BASE_DIR, "devices.json")
indexFile = os.path.join(BASE_DIR, "index.html")


class DeviceRegisterer:
    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri):
        if len(uri) == 0:
            return open(indexFile, "r").read()
        elif len(uri) == 1 and uri[0] == "devicesList":
            try:
                with open(devicesFile, "r") as f:
                    data = json.load(f)
                return json.dumps(data)
            except FileNotFoundError:
                raise cherrypy.HTTPError(404, f"File {devicesFile} not found")
        else:
            raise cherrypy.HTTPError(404, "Page not found")

    def POST(self, *uri):
        if len(uri) == 1 and uri[0] == "addDevice":
            try:
                body = cherrypy.request.body.read()
                new_device = json.loads(body)
                with open(devicesFile, "r") as f:
                    data = json.load(f)

                new_device_id = str(new_device.get("deviceID"))
                for d in data["devicesList"]:
                    if str(d.get("deviceID")) == new_device_id:
                        raise cherrypy.HTTPError(409, "Device ID already exists")
                    
                data["devicesList"].append(new_device)
                with open(devicesFile, "w") as f:
                    json.dump(data, f, indent=4)
                return json.dumps(data)
            except Exception as e:
                if isinstance(e, cherrypy.HTTPError):
                    raise e
                raise cherrypy.HTTPError(500, f"Internal Server Error: {str(e)}")
        else:
            raise cherrypy.HTTPError(404, "Page not found")

    def PUT(self, *uri):
        if len(uri) == 2 and uri[0] == "updateDevice":
            device_id_from_url = uri[1]
            try:
                body = cherrypy.request.body.read()
                updated_device_info = json.loads(body)
                with open(devicesFile, "r") as f:
                    data = json.load(f)
                found = False
                for d in data["devicesList"]:
                    if str(d["deviceID"]) == str(device_id_from_url):
                        d["deviceName"] = updated_device_info.get(
                            "deviceName", d["deviceName"]
                        )
                        d["measureType"] = updated_device_info.get(
                            "measureType", d["measureType"]
                        )
                        d["unit"] = updated_device_info.get("unit", d["unit"])
                        found = True
                        break
                if not found:
                    raise cherrypy.HTTPError(404, "Device not found")

                with open(devicesFile, "w") as f:
                    json.dump(data, f, indent=4)

                return json.dumps(data)

            except Exception as e:
                if isinstance(e, cherrypy.HTTPError):
                    raise e
                raise cherrypy.HTTPError(500, f"Internal Server Error: {str(e)}")
        else:
            raise cherrypy.HTTPError(404, "Page not found")

    def DELETE(self, *uri):
        if len(uri) == 2 and uri[0] == "deleteDevice":
            device_id_from_url = uri[1]
            try:
                with open(devicesFile, "r") as f:
                    data = json.load(f)

                initial_length = len(data["devicesList"])
                data["devicesList"] = [
                    d
                    for d in data["devicesList"]
                    if str(d["deviceID"]) != str(device_id_from_url)
                ]

                if len(data["devicesList"]) == initial_length:
                    raise cherrypy.HTTPError(404, "Device not found")

                with open(devicesFile, "w") as f:
                    json.dump(data, f, indent=4)

                return json.dumps(data)

            except Exception as e:
                if isinstance(e, cherrypy.HTTPError):
                    raise e
                raise cherrypy.HTTPError(500, f"Internal Server Error: {str(e)}")
        else:
            raise cherrypy.HTTPError(404, "Page not found")


if __name__ == "__main__":
    conf = {"/": {"request.dispatch": cherrypy.dispatch.MethodDispatcher()}}

    cherrypy.tree.mount(DeviceRegisterer(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
