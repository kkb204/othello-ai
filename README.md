# othello-ai
A web-based Othello game built with Python and Flask, featuring an AI opponent.

## Tech Stack
- Language: Python, HTML
- Tools/Frameworks: Flask

## Overview 
Othello is a two player game where each player is either the dark or light counter on the game board. The aim is the colour the game board with the most of your colour counter. The AI opponent usesa  greedy algorithm to select the move that maximises the number of counters flipped each turn.

## How to run
Since files are in different folders, the code in the ‘flask_game_engine_ai.py’ file needs to be changed so that the path to imported files matches those on your computer. Currently, this is what the code looks like: sys.path.append("/Users/kiritbhatti/Downloads/programming_coursework_2/Stage 1")
You need to change the path in the quotation marks to the path to the file on your computer.
To run the game, input  ‘cd “path to Stage 3 folder”’. Then, input ‘python flask_game_engine_ai.py’, which is the name of the file that runs the game. Terminal should then output the web address ‘http://127.0.0.1:5000/’. Open your browser and go to the address. This should load to the board.

## Features
- Two-player mode
- AI opponent
- Web-based interface playable in the browser
  
## What I learned 
This project introduced me to web development for the first time by learning how to use Flask to handle backend routing, and using HTML to structure the frontend. Integrating the game logic with a web interface taught me how frontend and backend components communicate, giving me a clearer understanding of full-stack development.
