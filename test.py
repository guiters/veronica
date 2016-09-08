from core.tor.Handlers import Tor, HTMLHandler
from getpass import getpass as gp

passwd = gp("Pass: ")

tor = Tor(password=passwd)
tor.authenticate()

html = HTMLHandler()

parsed_html = html.retrHTML(url="http://c3jemx2ube5v5zpg.onion/", raw=False)

elements = html.getElements()

#print(elements)

print(elements['title'])

#for a in elements['div']:

#	print "[+] ", a

for repeater in tor.getRepeaters():

	print(repeater['address'])