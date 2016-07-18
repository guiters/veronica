import socket
import os

class Test:
    """ Handler para testing de proxies """
    
    def proxyChecker(self, proxyList = ("/etc/tor/torrc", "/etc/polipo/config", "/etc/privoxy/config")):
        
        proxyMissing = []
        
        for proxy in proxyList:
            
            if not os.path.exists(proxy):
                proxyMissing.append(proxy)
                
        if not proxyMissing:
            return (True, ())
        else:
            return (False,tuple(proxyMissing))
    
    def testConnectionProxy(self, address="127.0.0.1", ports={'tor': 9050, 'polipo':8123 , 'privoxy': 8118}):
        
        try:
        
            socket.setdefaulttimeout(5)
            
            for service, port in ports.items():
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((address, port))
                s.close()
                
            return True
        
        except socket.timeout:
            
            return False
