import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 5000))
    while True:
        data = s.recv(1024)
        print(data.decode(), end='')
        if data.endswith(b'move (0-8): '):
            move = input()
            s.sendall(move.encode())
        elif data.endswith(b'wins!\n') or data.endswith(b'Draw!\n'):
            break