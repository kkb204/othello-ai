""" This module controls the move that the AI opponent chooses to take """

import sys
import copy
sys.path.append("/Users/kiritbhatti/Downloads/programming coursework 2/Stage 1")
from components import legal_move, flip_counters

def find_legal_moves(board):
    """ Find the best move possible """
    temp_board = copy.deepcopy(board)
    available_moves = []
    highest_flipped = -1
    best_move = None
    for i in range(1,9):
        for j in range(1,9):
            legal = legal_move('Light', (i, j), board)
            if legal is True:
                available_moves.append((i,j))
    for coord in available_moves:
        number_flipped = flip_counters('Light', coord, temp_board)
        if len(number_flipped) > highest_flipped:
            highest_flipped = len(number_flipped)
            best_move = coord

    return best_move
