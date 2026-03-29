import pytest

import sys
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")
from components import initialise_board, legal_move, flip_counters
from game_engine import cli_coords_input, check_moves_available, simple_game_loop

board = initialise_board()

def test_moves_available():
    assert check_moves_available('Dark ', board) == True
    assert check_moves_available('Light', board) == True

def test_flip_counters():
    assert legal_move('Dark ', (3,4), board) == True
    flip_counters('Dark ', (3,4), board)
    assert board[2][3] == 'Dark '


def test_no_legal_moves():
    # Fill the board with dark counters
    for i in range(8):
        for j in range(8):
            board[i][j] = 'Dark '
    # Place a None counter in the top corner
    board[0][0] = 'None '
    assert check_moves_available('Light', board) == False
