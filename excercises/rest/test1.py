import cherrypy

class HelloWorld(object):
    exposed = True

    def GET(self):
        return "HelloWorld"




if __name__ == "__main__":
    conf = {
        "/": {  # / represents the root URL of the application
            "request.dispatch": cherrypy.dispatch.MethodDispatcher()  #specifies how CherryPy should match incoming requests to our Python methods.
            #MethodDispatcher uses the HTTP method to select the corresponding Python method 
        }
    }

    cherrypy.tree.mount(HelloWorld(), "/", conf) #register the class as a Cherrypy application
    cherrypy.engine.start()
    cherrypy.engine.block()

