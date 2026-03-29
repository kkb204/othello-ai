""" This module allows the Othello/Reversi game to run, with an AI opponent. """

import sys
import json
from flask import Flask, render_template, request, jsonify

sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")
from components import initialise_board, flip_counters, legal_move
from game_engine import check_moves_available
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 3")
from ai import find_legal_moves

# Create the flask app
app = Flask(__name__)

# Initialise the game state
game_board = initialise_board()
current_player = 'Dark '
move_counter = {'Dark ': 60, 'Light': 60}

@app.route('/')
def home():
    """ Display the board """
    return render_template('othello_board_ai.html', game_board=game_board)

@app.route('/move', methods=["GET"])
def move():
    """ Handle the player's move """
    global current_player
    # Check if the currrent player has any legal moves
    legal_moves_left = check_moves_available(current_player, game_board)
    if legal_moves_left is True:
        # Get move coordinates from the request
        x = request.args.get('x', type=int)
        y = request.args.get('y', type=int)
        # Check if the chosen move is legal
        legal = legal_move(current_player, (y,x), game_board)
        if legal is True:
            # Update the game state if the move is legal
            move_counter[current_player] -= 1
            flip_counters(current_player, (y,x), game_board)
            current_player = next_player(current_player)
            # Check if the player's move counter is 0 or both players have no legal moves left
            if (
                move_counter[current_player] == 0
                or (
                    not check_moves_available('Dark ', game_board)
                    and not check_moves_available('Light', game_board)
                    )
            ):
                winner, light_count, dark_count = check_winner(game_board)
                # Return the winner information
                return jsonify({
                    "status": "game_over",
                    "winner": winner,
                    "board": game_board,
                    "finished": {"dark": dark_count, "light": light_count}
                })
            # Return the updated board and next player information
            return jsonify({
                "status": "success",
                "board": game_board,
                "player": current_player
            })
        # If the move is illegal, inform the user
        return jsonify({
            "status": "fail",
            "message": f"Illegal move at ({x}, {y})",
            "board": game_board,
            "player": current_player
        })

    # If there are no legal moves left, game over
    winner, light_count, dark_count = check_winner(game_board)
    return jsonify({
        "status": "game_over",
        "winner": winner,
        "board": game_board,
        "finished": {"dark": dark_count, "light": light_count}
    })

@app.route('/ai_move', methods=["GET"])
def ai_move():
    """ Allow the AI opponent to take a move """
    global current_player, game_board
    # Check if it is AI's move
    if current_player == 'Light':
        # Find a legal move to take
        ai_move = find_legal_moves(game_board)
        # Update the game state
        flip_counters(current_player, ai_move, game_board)
        move_counter[current_player] -= 1
        current_player = next_player(current_player)
        # Check if the AI opponent has no moves left or both players have no legal moves left
        if (
                move_counter[current_player] == 0
                or (
                    not check_moves_available('Dark ', game_board)
                    and not check_moves_available('Light', game_board)
                    )
            ):
            winner, light_count, dark_count = check_winner(game_board)
            return jsonify({
                "status": "game_over",
                "winner": winner,
                "board": game_board,
                "finished": {"dark": dark_count, "light": light_count}
            })
    else:
        return jsonify({"status": "fail", "message": "Not AI turn"})
    # Return the updated board and next player information
    placed_y, placed_x = ai_move
    return jsonify({
        "status": "success",
        "board": game_board,
        "player": current_player,
        "ai_move": {"x": placed_x, "y": placed_y}, 
    })

def next_player(player):
    """ Switch between players """
    if player == 'Dark ':
        player = 'Light'
    else:
        player = 'Dark '
    return player

def check_winner(board):
    """ Determine the winner """
    light_counter = 0
    dark_counter = 0
    # Count the number of counters for each player
    for row in board:
        for counter in row:
            if counter == 'Light':
                light_counter += 1
            if counter == 'Dark ':
                dark_counter += 1
    # Determine winner or draw
    if light_counter > dark_counter:
        return 'Light', light_counter, dark_counter
    if light_counter < dark_counter:
        return 'Dark ', light_counter, dark_counter

    return 'Draw', light_counter, dark_counter

@app.route("/save_game", methods = ["POST"])
def save_game():
    """ Save the current game state to JSON """
    data = request.get_json()
    game_log = data["log"]
    game_state = {
        "current_player": current_player,
        "game_board": game_board,
        "move_counters": move_counter,
        "game_log": game_log
    }
    # Saves the game state to a JSON file
    with open("game_state.json", "w", encoding="utf-8") as f:
        json.dump(game_state, f, indent=2)

    return jsonify({"success": True})

@app.route("/load_game")
def load_game():
    """ Load the game state from JSON """
    global current_player, game_board, move_counter
    # Retrieves the saved game state from the JSON file
    with open("game_state.json", "r", encoding="utf-8") as f:
        game_state = json.load(f)

    current_player = game_state["current_player"]
    game_board = game_state["game_board"]
    move_counter = game_state.get("move_counters", {})
    game_log = game_state.get("game_log", [])
    return jsonify({
        "board": game_board,
        "log": game_log
    })

# Run the flask app
if __name__ == '__main__':
    app.run()
