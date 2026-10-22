import cherrypy


class HelloWorld(object):
    exposed = True

    def GET(self, *uri, **params):   
        output = "Hello World"

        if len(uri) != 0:
            output += '<br>uri: ' + ','.join(uri)

        if params != {}:
            output += '<br>params: ' + str(params)

        return output


if __name__ == "__main__":

    conf = {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()
        }
    }

    cherrypy.tree.mount(HelloWorld(), "/", conf)
    #cherrypy.config.update({"server.socket_port": 8081})

    cherrypy.engine.start()
    cherrypy.engine.block()
