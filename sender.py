import socket

def send_socket(target: (str, int), buffer: str) -> None:
    ip, port = target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
        print("Sending evil buffer...")
        s.send(bytes(buffer + "\r\n", "latin-1"))
        print("Done!")
    except:
        print("Could not connect.")
