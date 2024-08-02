"""
Day 13 - AI Tic Tac Toe
"""

import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all(
        [board[i][2 - i] == player for i in range(3)]
    ):
        return True
    return False


def is_full(board):
    return all([cell != " " for row in board for cell in row])


def player_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column.")
            continue
        row, col = int(move[0]), int(move[1])
        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter a valid row and column.")
            continue
        if board[row][col] != " ":
            print("Cell already taken. Choose another!")
            continue
        break
    board[row][col] = "X"


def ai_move(board):
    available_move = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    move = random.choice(available_move)
    board[move[0]][move[1]] = "O"


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win :)")
            break
        if is_full(board):
            print("It's a tie!")
            break

        ai_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play()
