import pygame

class Render:
    def __init__(self):
        self.set_constants()
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Connect 4")
        self.screen.fill(self.WHITE)

    def set_constants(self):
        self.WIDTH = 700
        self.HEIGHT = 600
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 155, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)

    def draw_board(self, board, turn, update=True):
        # Draw a blue background
        self.screen.fill(self.BLUE)
        for row in range(6):
            for column in range(7):
                if board[row][column] == 'X':
                    # Draw a red circle
                    color = self.RED
                    pygame.draw.circle(self.screen, color, (column * 100 + 50, row * 100 + 50), 40)
                elif board[row][column] == 'O':
                    color = self.BLUE
                    pygame.draw.circle(self.screen, color, (column * 100 + 50, row * 100 + 50), 40)
                else:
                    color = self.GREEN
                    pygame.draw.circle(self.screen, color, (column * 100 + 50, row * 100 + 50), 40)
        if turn == 'X':
            color = self.RED
        else:
            color = self.BLUE
        # Draw a small circle to indicate whose turn it is in the top left about 10px big
        pygame.draw.circle(self.screen, color, (10, 10), 10)
        if update:
            pygame.display.update()

    def get_move(self, valid_moves, board, turn):
        previous_col = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    # Highlight the column the mouse is over
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = int(mouse_x / 100)
                    if column != previous_col:
                        self.draw_board(board, turn, update=False)
                    if column in valid_moves:
                        # Draw a green hollow rectangle over the column
                        pygame.draw.rect(self.screen, self.GREEN, (column * 100, 0, 100, 600), 5)
                    else:
                        # Draw a red hollow rectangle over the column
                        pygame.draw.rect(self.screen, self.RED, (column * 100, 0, 100, 600), 5)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = int(mouse_x / 100)
                    if column in valid_moves:
                        return column