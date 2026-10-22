
import cherrypy


def reverse_string(string1):
    string_reversed = string1[::-1]
    return string_reversed


class StringReverser(object):
    exposed = True

    
    def GET(self, *uri, **params):

        if len(uri) == 0:
            return "Please provide at least one word"

        list_reversed_uri = []

        for element_uri in uri:
            uri_reversed = reverse_string(element_uri)
            list_reversed_uri.append(uri_reversed)

        return str(list_reversed_uri)



if __name__ == "__main__":
    conf = {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    }

    cherrypy.tree.mount(StringReverser(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
