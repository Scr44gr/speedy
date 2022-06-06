__author__ = 'Scr44gr'

from dataclasses import dataclass
from typing import Dict, List

from speedy_client.core.speed_memory import NfSpeedMemory
from subprocess import Popen
from socket import socket, AF_INET, SOCK_STREAM

@dataclass
class UserData:
    user_name: str = ""
    ip_address: str = ""
    server_ip: str  = ""
    port: int   = 0

@dataclass
class ServerInfo:
    server_name: str = ""
    platform: str = ""
    version: str = ""
    user_counts: int = 0
    max_user_counts: int = 0
    server_start_time: str = ""
    server_ip: str = ""
    port = 10980

    def new(self, params: List):
        return ServerInfo(
            server_name=params[0],
            platform=params[1],
            version=params[2],
            user_counts=int(params[3]),
            max_user_counts=int(params[4]),
            server_start_time=params[5]
        )

    def to_dict(self):
        return {
            'server_name': self.server_name,
            'platform': self.platform,
            'version': self.version,
            'user_counts': self.user_counts,
            'max_user_counts': self.max_user_counts,
            'server_start_time': self.server_start_time
        }

class SpeedApi(NfSpeedMemory):

    def __init__(self, debug_mode: bool = False) -> None:
        super().__init__()
        self.pid = None
        self.game_process = None
        self._game_path: str = None
        self._debug_mode = debug_mode
        self.user_data = UserData()
        self.server_data = ServerInfo()
    
    def set_game_path(self, path: str) -> None:
        self._game_path = path

    def get_game_path(self) -> str:
        return self._game_path

    def open_game(self) -> bool:

        if not self.is_game_running() and not self._debug_mode:
            self.game_process = Popen([self.SPEED_PROCESS_NAME])
            self.pid = self.game_process.pid
            return (self.game_process is not None)
        
        self.game_process = Popen([self.SPEED_PROCESS_NAME])
        self.pid = self.game_process.pid
        self._start_process()
        return (self.game_process is not None)

    def get_game_current_ip(self) -> str:
        return self.get_on_memory_ip()

    def set_game_ip(self, ip: str) -> bool:

        result = self.write_ip(ip)
        if result:
            self.user_data.server_ip = ip
        return result

    def server_status(self) -> Dict:
        try:
            sock = socket.socket(AF_INET, SOCK_STREAM)
            sock.connect((self.server_data.server_ip, self.server_data.port))
    
            while (data := sock.recv(4024)) is not None:
                yield data
            sock.close()
        except (ConnectionRefusedError, ConnectionResetError):
            return {}

    def get_lists_of_servers(self) -> List:
        pass