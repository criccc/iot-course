import cherrypy


def reverse_string(string1):
    string_reversed = string1[::-1] 
    return string_reversed


class StringReverser(object):
    exposed = True

    def GET(self, *uri):

        if len(uri) == 0:
            return "Please provide a word in the URL"

        word = uri[0]           
        reversed_word = reverse_string(word)

        return reversed_word


if __name__ == "__main__":
    conf = {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    }

    cherrypy.tree.mount(StringReverser(), "/", conf)
    cherrypy.config.update({"server.socket_port": 8081})

    cherrypy.engine.start()
    cherrypy.engine.block()
