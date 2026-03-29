""" This module contains functions to run the game for the user. """

from components import initialise_board, print_board, legal_move, flip_counters

def cli_coords_input():
    """ Take coordinates as input and validate them. """
    valid = False
    # Continue asking for coordinates until they are valid
    while valid is False:
        try:
            # Prompt the user to enter x and y coordinates
            x_coord = int(input("enter your x coordinate "))
            y_coord = int(input("enter your y coordinate "))
            # Check the coordinates are in the range
            if 1 <= x_coord <= 8 and 1 <= y_coord <= 8:
                valid = True
            else:
                print("Coordinates are not in range.")
        # If the value is not an integer, inform the user
        except ValueError:
            print("Invalid input. Please enter integers.")

    # Return the coordinates as a tuple
    return (x_coord, y_coord)

def check_moves_available(colour, board):
    """ Check if there are legal moves available for a given player """
    size = len(board)
    # Check each space on the board
    for x in range(1, size+1):
        for y in range(1, size+1):
            # If placing a counter here is a legal move, return True
            legal = legal_move(colour, (x,y), board)
            if legal is True:
                return True
    # No legal moves found
    return False

# A function to allow the full game to run
def simple_game_loop():
    """ Allow the full game to run in a loop """
    print("Welcome to Othello")
    board = initialise_board()
    # Output the initial state of the board
    print_board(board)

    current_player_index = 0
    legal_moves_left = True

    # Initialise player details in dictionaries
    player_1 = {"colour": "Dark ", "move_counter": 60}
    player_2 = {"colour": "Light", "move_counter": 60}
    # A list to help with whose go is next
    players = [player_1, player_2]
    player = players[current_player_index]

    while True:
         # Check if both players have legal moves left and the current player has moves left
        if player["move_counter"] == 0 or (not check_moves_available('Dark ', board) and not check_moves_available('Light', board)):
            break
        # Retrieve the colour of the current_player
        player_colour = player["colour"]
        print(f"Please place a {player_colour} counter on the board")
        if check_moves_available(player_colour, board) is True:
            # Prompt a valid input
            coordinates = cli_coords_input()
            # Outflank counters, if the move is legal
            if legal_move(player_colour, coordinates, board) is True:
                flip_counters(player_colour, coordinates, board)
                print_board(board)
                player["move_counter"] -= 1
                # Move to the next player (switches between a 0 and 1 index)
                current_player_index = 1 - current_player_index
                player = players[current_player_index]
            else:
                print("Illegal move. Try again.")
        else:
            legal_moves_left = False
        move_counter = player["move_counter"]

    dark_count = 0
    light_count = 0
    # Count the number of light and dark counters
    for row in board:
        for square in row:
            if square == "Light":
                light_count += 1
            if square == "Dark ":
                dark_count += 1

    # Check who the winner is (The player with more counters on the board)
    if dark_count > light_count:
        print("The winner is the player with the dark coloured counters")
        print(f"dark counters: {dark_count}\n light counters: {light_count}")
    elif light_count > dark_count:
        print("The winner is the player with the light coloured counters")
        print(f"dark counters: {dark_count}\n light counters: {light_count}")
    else:
        print("It was a draw!")
        print(f"dark counters: {dark_count}\n light counters: {light_count}")

if __name__ == "__main__":
    simple_game_loop()
