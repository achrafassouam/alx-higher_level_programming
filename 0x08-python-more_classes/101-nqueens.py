#!/usr/bin/python3
import sys


def print_board(board):
    for row in board:
        print(" ".join(row))


def is_valid(board, row, col):
    for i in range(len(board)):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(n, board, col):
    if col >= n:
        print_board(board)
        return

    for i in range(n):
        if is_valid(board, i, col):
            board[i][col] = 'Q'
            solve_nqueens(n, board, col+1)
            board[i][col] = '.'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = 0
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for i in range(n)] for j in range(n)]
    solve_nqueens(n, board, 0)
