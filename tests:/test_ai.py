import pytest

import sys
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 3")
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")

from ai import find_legal_moves
from components import initialise_board, legal_move, flip_counters

board = initialise_board()

def test_legal_ai_move():
    ai_coords = find_legal_moves(board)
    assert legal_move('Light', ai_coords, board) == True

def test_ai_flips():
    ai_coords = find_legal_moves(board)
    # Flip counters according the AI move
    flip_counters('Light', ai_coords, board)
    dark_count = 0
    light_count = 0
    # Count the number of each colour
    for row in board:
        for counter in row:
            if counter == 'Dark ':
                dark_count += 1
            elif counter == 'Light':
                light_count += 1
    # The AI opponent should have more than 2 counters to show flipping
    assert light_count > 2

