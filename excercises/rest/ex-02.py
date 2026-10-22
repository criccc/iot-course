import cherrypy
import json


def reverse_string(string1):
    return string1[::-1]


class StringReverser(object):
    exposed = True

    def PUT(self):
        # Read the request body
        body = cherrypy.request.body.read()

        # Convert JSON into a Python dictionary
        data = json.loads(body)

        # Create a dictionary for reversed values
        reversed_data = {}

        for key, value in data.items():
            reversed_data[key] = reverse_string(value)

        # Convert the Python dictionary into JSON
        output = json.dumps(reversed_data)

        #tells client that response body contains json
        cherrypy.response.headers["Content-Type"] = "application/json"

        return output.encode("utf-8") #.encode('utf-8') converts the JSON string into bytes for transmission in the HTTP response.


if __name__ == "__main__":
    conf = {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    }

    cherrypy.tree.mount(StringReverser(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
