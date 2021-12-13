import socket
import sys
import time


def fuzz(target: (str, int), timeout: int, prefix: str = "", postfix: str = "", step_size: int = 100, sleep: int = 1):
    """ A simple fuzzer. """

    ip, port = target
    size = step_size

    while True:
        buffer = prefix + "A" * size + postfix
        buffer_size = len(buffer) - len(prefix) - len(postfix)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                # s.recv(1024)

                print("Fuzzing with {} bytes".format(buffer_size))
                s.send(bytes(buffer, "latin-1"))
                # s.recv(1024)

        except Exception as e:
            print(e)
            print("Fuzzing crashed at {} bytes".format(buffer_size))
            sys.exit(0)

        size += step_size
        time.sleep(sleep)
