import socket

HOST = '127.0.0.1'  # IP адрес сервера
PORT = 65432        # Порт сервера

# Создание клиентского сокета
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Подключение к серверу')
    while True:
        # Ожидание начала игры
        data = s.recv(1024)
        if data.decode('utf-8') == 'START':
            print('Игра началась')
            break
    while True:
        # Ожидание хода
        data = s.recv(1024)
        if data.decode('utf-8') == 'TURN':
            print('Ваш ход (введите число от 0 до 8):')
            move = input()
            s.sendall(bytes(move, 'utf-8'))
        elif data.decode('utf-8') == 'INVALID':
            print('Некорректный ход, попробуйте еще раз')
        elif data.decode('utf-8') == 'WINNER':
            # Определение победителя и вывод результата
            data = s.recv(1024)
            winner = int(data.decode('utf-8'))
            if winner == 1:
                print('Победил игрок 1')
            else:
                print('Победил игрок 2')
            break
        elif data.decode('utf-8') == 'DRAW':
            # Ничья
            print('Ничья')
            break
        else:
            # Обновление игрового поля
            game_board = eval(data.decode('utf-8'))
            print('-------------')
            print('|', game_board[0], '|', game_board[1], '|', game_board[2], '|')
            print('-------------')
            print('|', game_board[3], '|', game_board[4], '|', game_board[5], '|')
            print('-------------')
            print('|', game_board[6], '|', game_board[7], '|', game_board[8], '|')
            print('-------------')
