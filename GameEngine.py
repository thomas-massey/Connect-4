from time import sleep
import RenderEngine
import AI

class Board:
    def __init__(self, no_render=False, board=None):
        # 0,0 is top left and it is 7 columns and 6 rows
        if board == None:
            self.board = [[None for _ in range(7)] for _ in range(6)]
        else:
            self.board = board
        self.turn = 'X'
        self.winner = None
        self.is_game_active = True
        if not no_render:
            self.render = RenderEngine.Render()
            self.is_against_AI = self.render.is_against_AI()
            if self.is_against_AI:
                self.player = self.render.get_player()
                self.AI_Mode = self.render.get_AI_mode()
        

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
        if not self.is_against_AI:
            return self.render.get_move(valid_moves, self.board, self.turn)
        else:
            if self.turn == self.player:
                return self.render.get_move(valid_moves, self.board, self.turn)
            else:
                if self.AI_Mode == 'Random':
                    return AI.random_move(valid_moves)
                elif self.AI_Mode == 'Depth3':
                    return AI.depth_3(self.board, valid_moves, self.turn)
                elif self.AI_Mode == 'Depth5':
                    return AI.depth_5(self.board, valid_moves, self.turn)

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = self.turn
                break
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        print(self.board)

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