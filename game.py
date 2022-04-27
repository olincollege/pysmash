from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_view import TextView
from tic_tac_toe_controller import TextController


from player import Player
from view import TextView
from controller import TextController

def main():
    """
    Creates a `TicTacToeBoard` instance,
    a `TextView` instance and two `TextControllers`
    instances to represent the game board.
    Gets moves from each player until either one player has won,
    or until the board is full. Prints who won or that the
    game was a draw

    Returns: nothing to break out of the while loop.
    """
    player = Player()
    view = TextView(player)
    player1 = TextController(player)
    player2 = TextController(player)
    

if __name__ == "__main__":
    main()
