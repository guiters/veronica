from exception.TorExceptions import TorConnectionException

class Tor:
    """ Handler de control de instancia de Tor """
	
    def __init__(self, port=9051, password=""):
        
        self.__password = password
        self.__port=port
        
    def authenticate(self):
        
        try:
            
            from stem.control import Controller
            
        except:
            
            raise TorConnectionException("Stem Package Missing")
            
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
            
            repeaters.append({'nickname': router.nickname, 'address': router.address, 'date_published': router.published, 'bandwidth': router.bandwidth, 'digest': router.digest, 'fingerprint': router.fingerprint, 'or_port': router.or_port})
            
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
                
                exitNodes.append({'nickname': node.nickname, 'address': node.address, 'fingerprint': node.fingerprint, 'platform': node.platform, 'os': node.operating_system, 'burst': node.burst_bandwidth, 'estimated': node.observed_bandwidth, 'circuit_protocols': node.circuit_protocols, 'contact': node.contact, 'tor_version': node.tor_version})
            
            else:
                
                pass
                
        return tuple(exitNodes)