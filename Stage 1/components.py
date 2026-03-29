""" This module contains logic for Othello/Reversi game. """
""" It includes functions such as, board initialisation and player move. """


# A list for each counter around the chosen one
# Used in legal_move and flip_counters
surrounding_counters = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def initialise_board(size=8):
    """ Set up a 2D array with the number of rows and columns as the size given. """
    board = []
    # Append 8 empty lists to the board
    for i in range(0, size):
        board.append([])
        # Append 'None' 8 times to each list
        for j in range(0, size):
            board[i].append('None ')
    # Place the four initial counters in the centre of the board
    centre = int(size/2)
    board[centre-1][centre-1] = 'Light'
    board[centre-1][centre] = 'Dark '
    board[centre][centre-1] = 'Dark '
    board[centre][centre] = 'Light'

    return board

def print_board(board):
    """ Display the board to the user, with numbered rows and columns."""
    # Calculate the number of columns
    size = len(board[0])
    column_numbers = []
    # Add numbers for each column in the board
    for i in range(1, size+1):
        column_numbers.append(str(i))
    # Join each number with 5 spaces between
    numbers = "     ".join(column_numbers)
    # Output column numbers on the first line
    print(" ", numbers)
    row_count = 1
    # Traverse through each row in the 2D array
    for row in board:
        # Join the values in each row with a space
        values = " ".join(row)
        # Output the row number with the values succeeding
        print(row_count, values)
        # Move to the next row
        row_count += 1

def legal_move(colour, coordinate, board):
    """ Check if a given move is legal. """
    x, y = coordinate
    size = len(board)
    # Convert the coordinates into list indices
    x = x-1
    y = y-1
    # Check if the chosen space is empty
    if board[x][y] != 'None ':
        return False

    # Check each direction from the chosen square
    for sx, sy in surrounding_counters:
        surrounding_x = x+sx
        surrounding_y = y+sy
        found_opponent = False
        # Check that the next square in this direction is still on the board
        while 0 <= surrounding_x < size and 0 <= surrounding_y < size:
            value = board[surrounding_x][surrounding_y]
            # Checks if the counter is the opponents counter
            if value != colour and value != 'None ':
                found_opponent = True
                # Moves in the same direction as the opponents counter
                surrounding_x += sx
                surrounding_y += sy
            # If we reach our own colour after at least one opponent piece, the move is legal
            elif value == colour:
                if found_opponent:
                    return True
                else:
                    break
            else:
                # Reached an empty square
                break
    return False

def flip_counters(colour, move, board):
    """ Allow counters to be outflanked when a player takes their move. """
    x, y = move
    size = len(board)
    # Convert the coordinates into list indices
    x = x-1
    y = y-1
    # Place a counter in the chosen position
    board[x][y] = colour

    to_flip_copy = []

    # Check each direction from the chosen square
    for sx, sy in surrounding_counters:
        surrounding_x = x+sx
        surrounding_y = y+sy
        to_flip = []
        while 0 <= surrounding_x < size and 0 <= surrounding_y < size:
            value = board[surrounding_x][surrounding_y]
            # Checks if the counter is the opponents counter
            if value != colour and value != 'None ':
                # Add the opponents counter to the list to flip
                to_flip.append((surrounding_x, surrounding_y))
            # Check if we reach our own colour after at least one opponent piece
            elif value == colour and value != 'None ':
                # Check if there are counters to flip
                if to_flip:
                    to_flip_copy.extend(to_flip)
                    # Flip the counters to the players colour
                    for fx, fy in to_flip:
                        board[fx][fy] = colour
                break
            else:
                break
            # Moves in the same direction as the opponents counter
            surrounding_x += sx
            surrounding_y += sy
    # Use in the AI opponent functions
    return to_flip_copy
