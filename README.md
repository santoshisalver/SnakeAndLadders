# Snake & Ladders Game in Python

## Overview

This is a simple Python implementation of the classic **Snake & Ladder** game. 
The game allows two players to take turns rolling a dice and moving their respective pieces across the board.
The board is displayed using an image, and the game logic takes care of applying ladders and snakes to either boost or reduce the player's score.

## Features

- **Board Image**: The game starts by loading a classic Snake & Ladder board image using the **PIL (Pillow)** library, showing the traditional grid with snakes and ladders.
- **Player Interaction**: The program asks for the names of two players, allowing them to play against each other.
- **Dice Roll**: Players take turns rolling a virtual dice. The dice generates a random number between 1 and 6, determining how many steps the player moves forward on their turn.
- **Ladders and Snakes**: The game automatically handles the effects of landing on a ladder or a snake:
  - **Ladders**: If a player lands on a ladder, they are moved forward to a higher number, accelerating their progress.
  - **Snakes**: If a player lands on a snake, they are pulled back to a lower position.
- **Victory Condition**: The game continues until one player reaches 30 points (the end of the board), at which point the program announces the winner.

  ## Example Output

Here is an example of what the gameplay output looks like when two players are playing:

Player one, please enter your name: santoshi Player two, please enter your name: saipriya

santoshi, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 2 santoshi your score: 2

saipriya, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 2 saipriya your score: 2

santoshi, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 1 Ladder santoshi your score: 22

saipriya, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 1 Ladder saipriya your score: 22

santoshi, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 1 santoshi your score: 23

saipriya, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 2 saipriya your score: 24

santoshi, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 6 Snake santoshi your score: 20

saipriya, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 4 saipriya your score: 28

santoshi, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 4 santoshi your score: 24

saipriya, your turn Press 1 to continue, 0 to quit: 1 Dice showed: 3 saipriya your score: 30 saipriya won
