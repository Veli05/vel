import socket

HOST = '127.0.0.1'  # IP адрес сервера
PORT = 65432        # Порт сервера

# Создание серверного сокета
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Сервер запущен')
    conn1, addr1 = s.accept()
    print('Игрок 1 подключен:', addr1)
    conn2, addr2 = s.accept()
    print('Игрок 2 подключен:', addr2)
    # Отправка сообщения об начале игры
    conn1.sendall(b'START')
    conn2.sendall(b'START')
    # Инициализация игрового поля
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Определение победных комбинаций
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    # Определение текущего игрока и хода
    current_player = conn1
    current_move = 'X'
    while True:
        # Отправка игрового поля текущему игроку
        current_player.sendall(bytes(str(game_board), 'utf-8'))
        # Отправка сообщения о ходе текущего игрока
        current_player.sendall(b'TURN')
        # Получение хода от текущего игрока
        data = current_player.recv(1024)
        move = int(data.decode('utf-8'))
        # Проверка корректности хода
        if game_board[move] != ' ':
            current_player.sendall(b'INVALID')
            continue
        # Обновление игрового поля
        game_board[move] = current_move
        # Проверка наличия победной комбинации
        for combination in win_combinations:
            if game_board[combination[0]] == game_board[combination[1]] == game_board[combination[2]] != ' ':
                # Определение победителя и отправка сообщения
                if current_player == conn1:
                    conn1.sendall(b'WINNER')
                    conn1.sendall(bytes(str(1), 'utf-8'))
                    conn2.sendall(b'WINNER')
                    conn2.sendall(bytes(str(1), 'utf-8'))
                else:
                    conn1.sendall(b'WINNER')
                    conn1.sendall(bytes(str(2), 'utf-8'))
                    conn2.sendall(b'WINNER')
                    conn2.sendall(bytes(str(2), 'utf-8'))
                break
        else:
            # Проверка наличия свободных клеток
            if ' ' not in game_board:
                # Ничья
                conn1.sendall(b'DRAW')
                conn2.sendall(b'DRAW')
                break
            # Смена текущего игрока и хода
            if current_player == conn1:
                current_player = conn2
                current_move = 'O'
            else:
                current_player = conn1
                current_move = 'X'
