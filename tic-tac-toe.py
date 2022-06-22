import sys
import time
import random

X="X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

#Инструкция
def display_instruct():
    """Выводит инструкцию"""
    print("""
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)
def ask_yes_no(question):
    """Спрашивает... ответ yes или no"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response
def ask_number(question):
    """Спрашивает число в диапазоне от 0 до 8"""
    response = None; low = 0; high =8
    while response not in range(low,high+1):
        response = int(input(question))
        if response not in range(low,high+1):
            print("Введите число от 0 до 8!")
    return response
def pieces():
    """Определяет первый ход вопросом"""
    who_first = ask_yes_no("Хочешь ходить первым?(y или n):")
    if who_first == "y":
        print("Хорошо, играй крестиками(Ты ходишь первый)"); human = X;computer = O
    else: print("Хорошо, играй ноликами(Комп. ходит первым)"); human = O;computer = X
    return computer,human
def pieces_2():
    """Оперделяет первый ход через случайн. число"""
    print("Определяю кто первый")
    for i in [1,2,3,4,5,6,7,8,9,10,".",".",".","."]:
        print(i,end=" ")
        sys.stdout.flush()
        time.sleep(0.2)
    random_=random.randint(0,1)
    if random_ == 0:
        print("Случайное число определило первого им оказался---",end = " ");time.sleep(2);print("Ты!");print("Играй крестиками")
        human = X; computer = O
    else:
        print("Случайное число определило первого им оказался---",end = " ");time.sleep(2);print("Компютер!");print("Играй ноликами")
        human = O;computer = X
    return computer,human
def new_board():
    """Создаёт игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
def display_board(board):
    """Отображает доску на экране"""
    print("\n\t",board[0],"|",board[1],"|",board[2]);print("\t","---------");print("\t",board[3],"|",board[4],"|",board[5]);print("\t","---------");print("\t",board[6],"|",board[7],"|",board[8]);print("\t","---------")
def legal_moves(board):
    """Создаёт список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
def human_move(board,human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
       move = ask_number("Введите номер поля в которое хотите сделать ход")
       if move not in legal:
           print("Это поле занято! Выберите другое")
    print("Поле которое вы выбрали--", move)
    return move
def computer_move(board,computer,human):
    """Делает ход за компютер"""
    #Создадим копию доски
    board = board[:]
    #Поля от лучшего к худшему
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer#помещает в доступные поля свой тип фишек
    #если следующим ходом может победить компьютер,выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        #выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move]=human#помещает в свободные поля тип фишек человека
        #если следующим ходом может победить человек, болкируем этот ход
        if winner(board) == human:
            print(move)
            return move
        #отменим изменения
        board[move]=EMPTY
    #поскольку следующим ходом ни одна сторона не может победить
    #Выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else: return X
def congrat_winner(the_winner,computer,human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print("Три",the_winner,"в ряд")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил компьютер!\n","Ничего в следующий раз повезёт")
    elif the_winner == human:
        print("Победил человек!\n","Поздравляем!")
    elif the_winner == TIE:
        print("Ничья\n","Как неожиданно!")
def main():
    display_instruct()
    computer,human = pieces_2()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        elif turn == computer:
            move = computer_move(board,computer,human)
            board[move]=computer
        display_board(board)
        turn=next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer,human)

#запуск
main()

a = input("Enter чтобы выйти")
