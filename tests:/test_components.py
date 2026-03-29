import pytest

import sys
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")
from components import initialise_board, legal_move

board = initialise_board()


def test_board_size():
    # Check there are 8 rows
    assert len(board) == 8
    # Check there are 8 spaces in each row
    for row in board:
        assert len(row) == 8

def test_initial_counters():
    assert board[3][3] == 'Light'
    assert board[3][4] == 'Dark '
    assert board[4][3] == 'Dark '
    assert board[4][4] == 'Light'

def test_legal_move_identified():
    # Check if a dark counter placed at (3,4) is legal
    assert legal_move('Dark ', (3,4), board) == True

def test_illegal_move_identified():
    # Check if a dark counter places at (1,1) is legal
    assert legal_move('Dark ', (1,1), board) == False
