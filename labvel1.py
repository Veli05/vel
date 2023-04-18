import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
print(s.getsockname()[0])
