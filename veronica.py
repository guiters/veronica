#!/usr/bin/env python

import sys

def main():

	if len(sys.argv) < 2:
		print("""[-] Error: Insufficient arguments.

Usage: """ + sys.argv[0] + """ [cli|web]

	-cli:	Console Mode.
	-web:	Web-based Mode.
""")

	else:

		if sys.argv[1] == "cli":

			execfile("cli/cli.py")

		elif sys.argv[1] == "web":

			execfile("web/web.py")

		else:

			print("[-] Illegal argument.")

if __name__ == "__main__":
	main()