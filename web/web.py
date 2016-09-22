#!/usr/bin/env python

import cherrypy
from jinja2 import Environment, FileSystemLoader
import sqlite3 as sq
import os

try:
	templates_path = os.getenv("VERONICA_WEB_TEMPLATES")
except:
	templates_path = "templates"

env = Environment(loader=FileSystemLoader(templates_path))

class Root:

	def __init__(self):

		self.__user = "anonymous"

	#@cherrypy.expose
	def index(self):

		index.exposed = True

		template = env.get_template('index.html')

		instance = {

			'user': self.__user

		}

		return template.render(instance=instance)

if __name__ == "__main__":

	conf = {
		
		'/': {

			'tools.sessions.on': True

		}

	}

	cherrypy.quickstart(Root(), '/', conf)