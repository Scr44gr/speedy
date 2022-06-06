from typing import Dict, List
from speedy_client.core.speed import SpeedApi
from re import compile, Pattern

class ServerValidator:
    PATTERN_IP_ADDRESS: Pattern = compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    @classmethod
    def is_valid_address(cls, address: str) -> bool:

        return (cls.PATTERN_IP_ADDRESS.match(address) is not None)

class JsProxy:

    def __init__(self):
        
        self.speed_api: SpeedApi = SpeedApi()

    def getServersList(self) -> List:
        return self.speed_api.get_lists_of_servers()
    
    def getServerInfo(self, server_id: str) -> Dict:
        return self.speed_api.get_server_info(server_id)
    
    def setServerIp(self, server_id: str, ip_address: str) -> bool:
        result = False

        if ServerValidator.is_valid_address(ip_address):
            result = self.speed_api.set_game_ip(server_id, ip_address)

        return result
    
    def setGamePath(self, path: str = './Speed.exe'):

        self.speed_api.set_game_path(path)