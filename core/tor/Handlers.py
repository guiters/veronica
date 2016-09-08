# -*- coding: utf-8 -*-
from exception.TorExceptions import TorConnectionException
from exception.TorExceptions import MissingItem

import requests


class Tor:
    """ Handler de control de instancia de Tor """
	
    def __init__(self, port=9051, password=""):
        
        self.__password = password
        self.__port=port
        
    def authenticate(self):
        
        try:
            
            from stem.control import Controller
            
        except:
            
            raise MissingItem("Stem Package Missing")
            
        try:
            
            
            self.__controller = Controller.from_port(port=self.__port)
            self.__controller.authenticate(self.__password)
            return True
        
        except Exception as e:

            raise TorConnectionException(str(e))
            
    def getRepeaters(self):
            
        self.authenticate()
                     
        repeaterSet = self.__controller.get_network_statuses()
        
        repeaters = []
        
        for router in repeaterSet:
            
            repeaters.append({

                'nickname': router.nickname, 
                'address': router.address, 
                'date_published': router.published, 
                'bandwidth': router.bandwidth, 
                'digest': router.digest, 
                'fingerprint': router.fingerprint, 
                'or_port': router.or_port

                })
            
        return tuple(repeaters)
        
    def getExitNodes(self):
        
        try:
            from stem.descriptor.remote import DescriptorDownloader
        except:
            raise TorConnectionException("Stem Package Missing")
        
        #self.authenticate()
            
        downloader = DescriptorDownloader()
        
        exitNodes = []
        
        for node in downloader.get_server_descriptors().run():
            
            if node.exit_policy.is_exiting_allowed():
                
                exitNodes.append({

                    'nickname': node.nickname, 
                    'address': node.address, 
                    'fingerprint': node.fingerprint, 
                    'platform': node.platform, 
                    'os': node.operating_system, 
                    'burst': node.burst_bandwidth, 
                    'estimated': node.observed_bandwidth, 
                    'circuit_protocols': node.circuit_protocols, 
                    'contact': node.contact, 
                    'tor_version': node.tor_version

                    })
            
            else:
                
                pass
                
        return tuple(exitNodes)


class HTMLHandler:

    def __init__(self, proxies={'http': 'http://127.0.0.1:8118','https': 'https://127.0.0.1:8118'}):

        self.__proxies = proxies

    def retrHTML(self, url="google.com", raw=True, https=False, prettify=True):
        
        if https:

            protocol = "https://"

        else:

            protocol = "http://"    

        if not url.startswith(protocol):

            url = protocol + url

        self.__response = requests.get(url, proxies=self.__proxies)

        if self.__response.status_code == 200:

            if not raw:

                self.__response_text = self.__response.text.strip("\n").strip("\r")

            else:

                self.__response_text = self.__response.text

            if prettify:

                try:

                    from bs4 import BeautifulSoup

                    self.__soup = BeautifulSoup(self.__response_text)
                    self.__response_text = self.__soup.prettify()

                except:
            
                    raise MissingItem("BeatifulSoup Package Missing")

            return self.__response_text

        elif self.__response.status_code == 204:

            return "[+] No Content"

        elif self.__response.status_code == 205:

            return "[+] Reset Content"

        elif self.__response.status_code == 301 or self.__response.status_code == 302:

            return "[+] Moved Permanently"

        elif self.__response.status_code == 307:

            return "[+] Temporary Redirect"

        elif self.__response.status_code == 308:

            return "[+] Permanent Redirect"

        elif self.__response.status_code == 400:

            return "[+] Bad Request"

        elif self.__response.status_code == 401:

            return "[+] Unauthorized"

        elif self.__response.status_code == 402:

            return "[+] Payment Required"

        elif self.__response.status_code == 403:

            return "[+] Forbbiden"

        elif self.__response.status_code == 404:

            return "[+] Not Found"

        elif self.__response.status_code == 410:

            return "[+] Gone"

        elif self.__response.status_code == 500:

            return "[-] Internal Server Error"

        elif self.__response.status_code == 501:

            return "[-] Not Implemented"


        elif self.__response.status_code == 502:

            return "[-] Bad Gateway"


        elif self.__response.status_code == 503:

            return "[-] Service Unavailable"


        elif self.__response.status_code == 504:

            return "[-] Gateway Timeout"

        elif self.__response.status_code == 505:

            return "[+] HTTP Version Not Supported"

        else:

            return "[-] Unknown Error"

    def getElements(self):


        return {

            'title': self.__soup.title.string,
            'div': tuple(div for div in self.__soup.findAll('div')),
            'a': tuple(a for a in self.__soup.findAll('a')),
            'footer': tuple(footer for footer in self.__soup.findAll('footer')),
            'h1': tuple(h1 for h1 in self.__soup.findAll('h1')),
            'h2': tuple(h2 for h2 in self.__soup.findAll('h2')),
            'h3': tuple(h3 for h3 in self.__soup.findAll('h3')),
            'input': tuple(inputTag for inputTag in self.__soup.findAll('input')),
            'label': tuple(label for label in self.__soup.findAll('label')),
            'form': tuple(form for form in self.__soup.findAll('form')),
            'link': tuple(link for link in self.__soup.findAll('link')),
            'script': tuple(script for script in self.__soup.findAll('script')),
            'p': tuple(p for p in self.__soup.findAll('p')),
            'span': tuple(span for span in self.__soup.findAll('span')),
            'ul': tuple(ul for ul in self.__soup.findAll('ul')),
            'header': tuple(header for header in self.__soup.findAll('header')),
            'nav': tuple(nav for nav in self.__soup.findAll('nav')),
            'section': tuple(section for section in self.__soup.findAll('section')),
            'img': tuple(img for img in self.__soup.findAll('img')),
            'svg': tuple(svg for svg in self.__soup.findAll('svg'))

        }