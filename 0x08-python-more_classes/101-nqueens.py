#!/usr/bin/python3
"""This module solves the N Queens Problem using backtracking"""


import sys


def checkQueen(board, queen):
    """Check if a queen is not attacking the others

    Args:
        board (list of tuple of int): board placed so far
        queen (tuple): queen to check

    Returns:
        bool: True if queen is in correct position, False otherwise

    """

    for x, y in board:
        if y == queen[1]:
            return False
        if abs((y - queen[1]) / (x - queen[0])) == 1:
            return False
    return True


def fill_board(n, board, n_queens):
    """Fill the chess board with queens

    Args:
        n (int): number of board that need to be placed
        board (list of tuple of int): board placed so far
        n_queens (list of list of list of int): queen positions that work

    """
    if len(board) == n:
        n_queens.append([list(q) for q in board])
        return
    x = len(board)
    for y in range(n):
        queen = (x, y)
        if checkQueen(board, queen):
            board.append(queen)
            fill_board(n, board, n_queens)
            board.pop()


def main():
    """Entry point to solve N Queens problem"""

    size = len(sys.argv)
    if size != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = []
    n_queens = []
    fill_board(n, board, n_queens)
    print('\n'.join(str(q) for q in n_queens))


if __name__ == '__main__':
    main()
