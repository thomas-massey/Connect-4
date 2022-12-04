from time import sleep
import RenderEngine

class Board:
    def __init__(self):
        # 0,0 is top left and it is 7 columns and 6 rows
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.turn = 'X'
        self.winner = None
        self.is_game_active = True
        self.render = RenderEngine.Render()

    def get_possible_columns(self):
        possible_columns = []
        for column in range(7):
            if self.board[0][column] is None:
                possible_columns.append(column)
        return possible_columns

    def is_active(self):
        return self.is_game_active

    def draw_board(self):
        self.render.draw_board(self.board, self.turn)

    def get_move(self):
        valid_moves = self.get_possible_columns()
        return self.render.get_move(valid_moves, self.board, self.turn)

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = self.turn
                break
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def check_for_winner(self, last_column):
        # Get the row and column of the last move
        for row in range(6):
            if self.board[row][last_column] is not None:
                last_row = row
                break
        # Check for a horizontal win
        for column in range(4):
            if self.board[last_row][column] == self.board[last_row][column + 1] == self.board[last_row][column + 2] == self.board[last_row][column + 3] is not None:
                self.winner = self.board[last_row][column]
                self.is_game_active = False
                return self.winner
        # Check for a vertical win
        for row in range(3):
            if self.board[row][last_column] == self.board[row + 1][last_column] == self.board[row + 2][last_column] == self.board[row + 3][last_column] is not None:
                self.winner = self.board[row][last_column]
                self.is_game_active = False
                return self.winner
        # Check for a diagonal win
        for row in range(3):
            for column in range(4):
                if self.board[row][column] == self.board[row + 1][column + 1] == self.board[row + 2][column + 2] == self.board[row + 3][column + 3] is not None:
                    self.winner = self.board[row][column]
                    self.is_game_active = False
                    return self.winner
        for row in range(3, 6):
            for column in range(4):
                if self.board[row][column] == self.board[row - 1][column + 1] == self.board[row - 2][column + 2] == self.board[row - 3][column + 3] is not None:
                    self.winner = self.board[row][column]
                    self.is_game_active = False
                    return self.winner
        else:
            return None
    
    def draw_winner(self, winner):
        self.render.draw_winner(winner)
        play_again = self.render.play_again()
        if play_again:
            return True
        else:
            self.is_game_active = False
            return False