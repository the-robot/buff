import socket
import sys
import time


def fuzz(ip: str, port: int, timeout: int, prefix: str = ""):
    """ A simple fuzzer. """

    buffer = prefix + "A" * 100

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                s.recv(1024)
                print("Fuzzing with {} bytes".format(len(buffer) - len(prefix)))
                s.send(bytes(buffer, "latin-1"))
                s.recv(1024)
        except Exception as e:
            print(e)
            print("Fuzzing crashed at {} bytes".format(len(buffer) - len(prefix)))
            sys.exit(0)

        buffer += 100 * "A"
        time.sleep(1)
