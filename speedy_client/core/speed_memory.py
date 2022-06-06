__author__ = 'Scr44gr'
"""
We need to Inject the Ip address of the server into the NFS game.

so, we are accessing the memory of the game and writing it.
"""
from typing import List
import pymeow


class NfSpeedMemory:
    """This class help to solve the problem of the NFS game.
    """

    SPEED_PROCESS_NAME: str = "Speed.exe"
    IP_MEMORY_ADDRESS: int = 0x6F1F40

    def __init__(self):
        self._start_process()

    def _start_process(self):
        try:
            self.process = pymeow.process_by_name(self.SPEED_PROCESS_NAME)
        except:
            self.process = None

    def write_ip(self, address: str) -> bool:
        """
        Write ip address to memory.

        args:
            address: str - ip address
        returns: bool - True if the ip address is written to memory.
        """
        
        # firs we need to get the current ip address from the memory.
        on_memory_text: str = pymeow.read_string(self.process, self.IP_MEMORY_ADDRESS)

        # then we need to clear the memory.
        for i in range(0, len(on_memory_text)):
            pymeow.write_string(self.process, self.IP_MEMORY_ADDRESS+i, '\x00')
        
        # then we need to write the new ip address.
        for i in range(0, len(address)):
            pymeow.write_string(self.process, self.IP_MEMORY_ADDRESS+i, address[i])
        
        return pymeow.read_string(self.process, self.IP_MEMORY_ADDRESS) == address # return True if the ip address is written correctly.
    
    def get_on_memory_ip(self) -> str:
        """
        Get the ip address from the memory.

        returns: str - ip address.
        """
        default: str = "127.0.0.1"
        if self.is_game_running():
            return pymeow.read_string(self.process, self.IP_MEMORY_ADDRESS)
        return default

    def is_game_running(self) -> bool:
        """
        Check if the game is running.

        returns: bool - True if the game is running.
        """
        try:
            return (pymeow.process_by_name(self.SPEED_PROCESS_NAME) is not None)
        except:
            return

    def is_game_running_by_id(self) -> bool:
        """
        Check if the game is running.

        returns: bool - True if the game is running.
        """
        try:
            return (pymeow.process_by_id(self.pid) is not None)
        except:
            return

    def write_port(self, address: str) -> bool: ...

    def calc_adrress(self, address: int, offsets: List) -> bool: ...