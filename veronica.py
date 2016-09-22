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

			template = self.__env.get_template('index.html')

			instance = {

				'user': self.__user

			}

			return template.render(instance=instance)

		@cherrypy.expose
		def auth(self, user="anon", password="anon"):

			try:
				if cherrypy.session['authenticated']:

					return "<h2>User: " + self.__user + " is online</h2>"

			except:

				pass

			conn = sq.connect('db/data.db')
			print("Ok")

			cursor = conn.execute("select name, password from users")

			b = False

			for row in cursor:

				if row[0] == user and row[1] == password:

					self.__user = user
					b = True
					cherrypy.session['authenticated'] = True
					cherrypy.session['user'] = self.__user
					return "Authenticated"

			if not b:
				return "Forbbiden"


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