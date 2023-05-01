import socket

def print_board(board):
    print(' | '.join(board[:3]))
    print('-'*9)
    print(' | '.join(board[3:6]))
    print('-'*9)
    print(' | '.join(board[6:]))

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

def check_draw(board):
    return ' ' not in board

def start_game(conn1, conn2):
    board = [' '] * 9
    turn = 'X'
    print_board(board)
    while True:
        if turn == 'X':
            conn1.sendall(b'Your turn, X. Enter move (0-8): ')
            data = conn1.recv(1024)
            move = int(data.decode())
            if board[move] != ' ':
                conn1.sendall(b'Invalid move. Try again.\n')
                continue
        else:
            conn2.sendall(b'Your turn, O. Enter move (0-8): ')
            data = conn2.recv(1024)
            move = int(data.decode())
            if board[move] != ' ':
                conn2.sendall(b'Invalid move. Try again.\n')
                continue
        board[move] = turn
        print_board(board)
        if check_win(board):
            if turn == 'X':
                conn1.sendall(b'X wins!\n')
                conn2.sendall(b'X wins!\n')
            else:
                conn1.sendall(b'O wins!\n')
                conn2.sendall(b'O wins!\n')
            break
        elif check_draw(board):
            conn1.sendall(b'Draw!\n')
            conn2.sendall(b'Draw!\n')
            break
        turn = 'O' if turn == 'X' else 'X'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 5000))
    s.listen()
    print('Server listening on 127.0.0.1:5000')
    conn1, addr1 = s.accept()
    print('Connected to', addr1)
    conn2, addr2 = s.accept()
    print('Connected to', addr2)
    conn1.sendall(b'Welcome to Tic Tac Toe!\n')
    conn2.sendall(b'Welcome to Tic Tac Toe!\n')
    start_game(conn1, conn2)
