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

    def draw_board(self, board):
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
        pygame.display.update()