#!/usr/bin/env python3

from random import randrange

def initialise_board():
    board = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
    return board

def print_board(board):
    print(" {0} | {1} | {2} \n-----------\n {3} | {4} | {5} \n-----------\n {6} | {7} | {8} ".format(
        board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))

def update_board(player, move, board):
    for row in board:
            for i in range(len(row)):
                if row[i] == move:
                    row[i] = player
                    return board

def get_player_move(player, board):
    print_board(board)
    move = None
    while not move:
        move = input("Player {0}, which square would you like to take? ".format(player))
        try:
            if int(move) < 0 or int(move) > 8 or move == ' ':
                raise ValueError
        except:
            print("Please enter a valid number.")
            move = None

    board = update_board(player, move, board)
    return board

def get_computer_move(player, board):
    
    while is_empty_square(board):
        move = randrange(0, 8)
        move = str(move)
        try:
            for row in board:
                for square in row:
                    if square == move:
                        board = update_board(player, move, board)
                        return board
        except:
            continue

def game_won(player, board):
    for row in board: #check rows
        if row[0] == row[1] and row[1] == row[2] and row[0] == player:
            return True
    
    for column in range(len(board)): #check columns
        if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[0][column] == player:
            return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == player) or (board[2][0] == board[1][1] and board[1][1] ==board[0][2] and board[2][0] == player): #check diagonals
            return True
    return False

def is_empty_square(board): #are there any empty squares on the board?
    for row in board:
        for square in row:
            if square not in ("X", "O"):
                return True
    return False     

def switch_player (player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

def determine_winner (board):
    if game_won("X", board):
        print("Player {0} won!".format("X"))
    elif game_won("O", board):
        print("Player {0} won!".format("O"))
    else:
        print("It's a tie!")

def get_players ():
    players = None
    while not players:
        
        try:
            players = int(input(
                "How many players are there?\n'1' if against computer.\n'2' if against another human! "))
            if players < 1 or players > 2:
                raise ValueError
        except:
            print("Please enter '1' or '2'.")
            players = None

    return str(players)

def main():
    players = get_players()
    board = initialise_board()
    player = "X"
    while not game_won("X", board) and not game_won("O", board) and is_empty_square(board):
        if player == "X":
            board = get_player_move("X", board)
        elif players == '1' and player == "O":
            board = get_computer_move("O", board)
        elif players == '2' and player == "O":
            board = get_player_move("O", board)
        print(player)
        player = switch_player(player)
            
    print_board(board)
    determine_winner(board)

if __name__ == "__main__":
    main()
