from time import sleep
import RenderEngine

class Board:
    def __init__(self):
        # 0,0 is bottom left
        self.board = [[None for x in range(0, 7)] for y in range(0, 6)]
        self.turn = 'X'
        self.winner = None
        self.is_game_active = True
        self.render = RenderEngine.Render()

    def get_possible_columns(self):
        possible_columns = []
        for column in range(8):
            if self.board[7][column] is None:
                possible_columns.append(column)
        return possible_columns

    def is_active(self):
        return self.is_game_active

    def draw_board(self):
        self.render.draw_board(self.board)