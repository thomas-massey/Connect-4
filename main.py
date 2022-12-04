# This is a game of connect 4 using a 7x6 board

# We will make use of pygame to create the GUI

import GameEngine

if __name__ == '__main__':
    # Create a game object
    game = GameEngine.Board()
    # Run the game loop
    while game.is_active():
        game.draw_board()
        chosen_column = game.get_move()
        game.make_move(chosen_column)
        winner = game.check_for_winner(chosen_column) # 0 - Game is still active, 1 - X wins, 2 - O wins, 3 - Tie