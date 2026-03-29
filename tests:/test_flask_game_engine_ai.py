import pytest
import json
import sys

sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 3")
sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")
from flask_game_engine_ai import app, check_winner
from components import initialise_board, flip_counters

board = initialise_board()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def setup_game_file():
    data = {"game_board": initialise_board(), "current_player": "Dark"}
    with open("game_state.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

def test_webpage_loading(client):
    response = client.get('/')
    # Ensure the webpage loads correctly
    assert response.status_code == 200
    # Check the word Othello, in bytes, is on the webpage
    assert b'Othello' in response.data

def test_move_route_valid(client):
    # Coordinates for a known legal move on initial board
    response = client.get('/move', query_string={'x': 3, 'y': 4})
    data = json.loads(response.data)
    assert data['status'] in ['success', 'game_over']
    assert 'board' in data

def test_save_game(client):
    # Set the game state
    game_state = {"board": board, "current_player":'Dark ', "move_counters": {}}
    # Put the game state in the json file
    response = client.post('/save_game', data=json.dumps(game_state), content_type='application/json')
    # Check the game has been saved
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert data["success"] == True

def test_load_game_route(client, setup_game_file):
    # Check that a route exists 
    response = client.get('/load_game')
    assert response.status_code == 200
    # Load the game state
    data = json.loads(response.data.decode("utf-8"))
    assert 'board' in data
    assert 'log' in data

def test_winner_found():
    flip_counters('Dark ', (3,4), board)
    winner, light_count, dark_count = check_winner(board)
    assert winner == 'Dark '


