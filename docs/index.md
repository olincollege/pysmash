This game is a clone of the popular Super Smash Bros. Our goal for this project was to create a working Super Smash Bros clone that can be played over a server. We wanted to learn how to make a game utlizing networking and servers in python. We thought this project of Super Smash Bros would give us a perfect opportunity for this. The server aspect of this project is the most unique feature to the game because it is something that we were not taught in class. We implemented the model, view, and controller method to the game. 

# Video Demo
[![Game Demo](https://img.youtube.com/vi/AT6Lnmm4oP0/0.jpg)](https://youtu.be/AT6Lnmm4oP0)

# Full Project Presentation
[![Project Presentation](https://img.youtube.com/vi/1fjQp3s1X5s/0.jpg)](https://youtu.be/1fjQp3s1X5s)

## Installation

To install, first clone found [here](github.com/olincollege/pysmash) and ensure you have all necessary dependencies by running
```
pip install -r requirements.txt
```

## Quick Start Guide

### Local Multiplayer

Run `main.py` and select the 'local' option, select your characters, and play the game!

### Online Multiplayer

To play online, you must have a game server running. To start one, run `server.py`

1. To connect as a client to the game, run `main.py`, then select the online option.
2. In the terminal, input the local IP address of the server (you can obtain this by running `ifconifg` or `ip a` on a Linux server, or `iwconfig` on a Windows server)
3. Lastly, type in the name of the character you would like to play as (Marth, Mario, or Pikachu) in all lowercase letters. You will be reprompted if you enter an invalid name.

## Controls

### Player 1

Use the arrow keys to move, the / key for a tilt attack, and the . (period) key for a smash attack

### Player 2

Use WASD to move, the 1 key for a tilt attack, and the 2 key for a smash attack

Smash attacks are more powerful than tilt attacks, but they have a longer cooldown and leave you vulnerable. Choose wisely!

## Github Repo [here](github.com/olincollege/pysmash)

## External Resources
<https://realpython.com/python-sockets/>

<https://docs.python.org/3/library/asyncio.html> 
