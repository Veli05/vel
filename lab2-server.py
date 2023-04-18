import socket
import sys

sock = socket.socket()
ip = "localhost"
port = 9999
sock.bind((ip,port))
sock.listen(10)
print ('Сервер запущен. Для остановки работы, пожалуйста, нажмите сочетание клавиш ctrl+c')
while True:
	conn, addr = sock.accept()
	print ('соединение: ', addr)
	name_file = (conn.recv(1024)).decode ('UTF-8')
	o = open ('/root/l2/' + name_file,'wb')
	while True:
		d = conn.recv(1024)
		o.write(d)
		if not d:
			break
	o.close()
	conn.close()
	print ('файл получен')
sock.close()
