import socket
import sys

ip = "localhost"
port = 9999

sock = socket.socket()
sock.connect((ip, port))
file_name = "message2.txt"
sock.send((bytes(f_name, encoding = 'UTF-8')))
o = open ("/root/send/" + f_name, "rb")
d = o.read(1024)
while (d):
	sock.send(d)
	d = o.read(1024)
o.close()
sock.close()
