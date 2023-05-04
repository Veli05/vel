import socket
import threading

def receive_messages(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode(), end='')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 5000))
    t = threading.Thread(target=receive_messages, args=(s,))
    t.start()
    while True:
        data = input()
        s.sendall(data.encode())