"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibilities.add((i, j))
    
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    if row not in range(3) or col not in range(3):
        raise ValueError("Action out of bounds")
    elif board[row][col] is not EMPTY:
        raise ValueError("Action already taken")
    
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        if all(board[row][col] == O for row in range(3)):
            return O

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return -1
    elif winner(board) == O:
        return 1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def min_value(board):
    if (terminal(board)):
        return utility(board), None

    v = math.inf
    best_move = None

    for action in actions(board):
        value, _ = max_value(result(board, action))
        if value < v:
            v = value
            best_move = action 
            if v == -1:
                return v, best_move

    return v, best_move

def max_value(board):
    if (terminal(board)):
        return utility(board), None

    v = -math.inf
    best_move = None

    for action in actions(board):
        value, _ = min_value(result(board, action))
        if value > v:
            v = value
            best_move = action 
            if v == 1:
                return v, best_move

    return v, best_move
