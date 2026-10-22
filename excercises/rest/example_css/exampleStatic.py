import cherrypy
import os

class ExampleStatic(object):
	exposed=True
	def __init__(self): 
		pass
	def GET(self):
		return open("index.html") #html defines the structure of the webpage


if __name__ == '__main__':
	conf={   #where files can find the files
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.staticdir.root': os.path.abspath(os.getcwd()),  #the absolute path of the current working directory
				'tools.sessions.on':True,  #enables session managment in cherrypy which allows the server to remember info associated with the client across multiple HTTP requests
			},
		 '/css':{
			'tools.staticdir.on': True,
			'tools.staticdir.dir':'./css' #css defines how the webpage looks
		 },
		 '/js':{
			'tools.staticdir.on': True,
			'tools.staticdir.dir':'./js' #js defines how it behaves when user intracts with it
		 },
	}		
	cherrypy.tree.mount(ExampleStatic(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
