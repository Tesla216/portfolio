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
        numX = 0
        numO = 0
        i = 0


        while i < 3:
            j = 0
            while j < 3:
                if board[i][j] == X:
                    numX += 1
                elif board[i][j] == O:
                    numO += 1
                j += 1
            i += 1

        #print(numX, numO)
        if numX <= numO:
            #print('X Turn')
            return X
        else:
            #print('O Turn')
            return O

        raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                moves.append((i, j))
            j += 1
        i += 1
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] != EMPTY:
        raise NameError("SpaceTakenError")
    else:
        temp_board = copy.deepcopy(board)
        turn = player(board)
        temp_board[action[0]][action[1]] = turn
        return temp_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    lines = board + list(map(list, zip(*board)))  # Rows and columns
    lines.append([board[i][i] for i in range(3)])  # Diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # Anti-diagonal

    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == 3:
            return line[0]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    boardV = get_vertical(board)
    i = 0
    while i < 3:
        if board[i][0] != EMPTY:
            if board[i].count(board[i][0]) == len(board[i]):
                #print('Game Over4')
                return True
        i += 1
    i = 0
    while i < 3:
        if boardV[i][0] != EMPTY:
            if boardV[i].count(boardV[i][0]) == len(boardV[i]):
                #print('Game Over3')
                return True
        i += 1

    if board[0][0] == board [1][1] == board [2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
         #print('Game Over2')
         return True

    i = 0

    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                #print('Game not Over')
                return False
            j += 1
        i += 1
    #print('Game Over1')
    return True



    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    boardV = get_vertical(board)
    i = 0
    while i < 3:
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            if board[i][0] == X:
                return 1
            else :
                return -1
        i += 1
    i = 0
    while i < 3:
        if boardV[i][0] == boardV[i][1] == boardV[i][2] != EMPTY:
            if boardV[i][0] == X:
                return 1
            else:
                return -1
        i += 1

    if board[0][0] == board [1][1] == board [2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        if board[1][1] == X:
            return 1
        else:
            return -1

    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # No move possible, game over

    current_player = player(board)

    if current_player == X:
        best_value = -float('inf')
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action


def max_value(board):
    """
    Returns the max utility value of the board.
    """
    if terminal(board):
        return utility(board)

    value = -float('inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    """
    Returns the min utility value of the board.
    """
    if terminal(board):
        return utility(board)

    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value

def get_vertical(board):
     board_vertical = [[board[0][0], board[1][0], board[2][0]],
                       [board[0][1], board[1][1], board[2][1]],
                       [board[0][2], board[1][2], board[2][2]]]
     return board_vertical

