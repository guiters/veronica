#!/usr/bin/env python

import sys
import subprocess as sp
import os

def main():

	if len(sys.argv) < 2:
		print("""[-] Error: Insufficient arguments.

Usage: """ + sys.argv[0] + """ [cli|web]

	-cli:	Console Mode.
	-web:	Web-based Mode.
""")

	else:

		try:

			web_dir_path = os.getenv("VERONICA_WEB_DIR")

		except:

			print("[-] Error: Set VERONICA_WEB_DIR in environment variables.")

			sys.exit(1)

		os.chdir(web_dir_path)
		print(os.getcwd())

		if sys.argv[1] == "cli":

			execfile("cli/cli.py")

		elif sys.argv[1] == "web":

			#sp.Popen(["/"], stdin=sp.PIPE)
			execfile("web.py")

		else:

			print("[-] Illegal argument.")

if __name__ == "__main__":
	main()