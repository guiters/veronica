#!/usr/bin/env python

import sys
import os

def webserver():

	import cherrypy
	from jinja2 import Environment, FileSystemLoader
	import sqlite3 as sq

	class Root:

		def __init__(self):

			self.__user = "anonymous"

			try:
				templates_path = os.getenv("VERONICA_TEMPLATES")
				print(templates_path)
				if templates_path:
					pass
				else:
					raise BaseException
			except:
				templates_path = "templates"

			self.__env = Environment(loader=FileSystemLoader(str(templates_path)))


		@cherrypy.expose
		def index(self):

			#index.exposed = True

			template = self.__env.get_template('index.html')

			instance = {

				'user': self.__user

			}

			return template.render(instance=instance)

	conf = {
		
		'/': {

			'tools.sessions.on': True

		}

	}

	cherrypy.quickstart(Root(), '/', conf)


def main():

	if len(sys.argv) < 2:
		print("""[-] Error: Insufficient arguments.

Usage: """ + sys.argv[0] + """ [cli|web]

	-cli:	Console Mode.
	-web:	Web-based Mode.
""")

	else:

		if sys.argv[1] == "web":
			webserver()

		else:
			pass

if __name__ == "__main__":
	main()