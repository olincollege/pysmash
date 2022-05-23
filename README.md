# PySmash
A Python clone of Super Smash Bros playable over LAN

## Installation

To install, first clone this repo and ensure you have all necessary dependencies by running
```
pip install -r requirements.txt
```

## Quick Start

### Local Multiplayer

Run `main.py` and select the 'local' option, select your characters, and play the game!

### Online Multiplayer

To play online, you must have a game server running. To start one, run `server.py`

1. To connect as a client to the game, run `main.py`, then select the online option.
2. In the terminal, input the local IP address of the server (you can obtain this by running `ifconifg` or `ip a` on a Linux server, or `ipconfig` on a Windows server)
3. Lastly, type in the name of the character you would like to play as (Marth, Mario, or Pikachu) in all lowercase letters. You will be reprompted if you enter an invalid name.

## Controls

### Player 1

Use the arrow keys to move, the / key for a tilt attack, and the . (period) key for a smash attack

### Player 2

Use WASD to move, the 1 key for a tilt attack, and the 2 key for a smash attack

Smash attacks are more powerful than tilt attacks, but they have a longer cooldown and leave you vulnerable. Choose wisely!

For more info, see our website [here](https://olincollege.github.io/pysmash)


