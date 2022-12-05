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
                    color = self.YELLOW
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

    def draw_winner(self, winner):
        # Draw a winner screen
        self.screen.fill(self.WHITE)
        if winner == 'X':
            color = self.RED
        else:
            color = self.YELLOW
        text = pygame.font.SysFont('comicsans', 100).render(f'{winner} Wins!', True, color)
        # Center the text
        self.screen.blit(text, (self.WIDTH / 2 - text.get_width() / 2, self.HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(3000)

    def is_against_AI(self):
        # Draw a two player screen
        self.screen.fill(self.WHITE)
        text = pygame.font.SysFont('comicsans', 100).render('Play against...', True, self.BLACK)
        # On the left have a human and on the right have an AI separated by a line
        human = pygame.font.SysFont('comicsans', 50).render('Human', True, self.RED)
        ai = pygame.font.SysFont('comicsans', 50).render('AI', True, self.BLUE)
        pygame.draw.line(self.screen, self.BLACK, (350, 300), (350, 600), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 300), (700, 300), 5)
        self.screen.blit(text, (self.WIDTH / 2 - text.get_width() / 2, 100))
        # Middle of lower half of screen
        self.screen.blit(human, (85, 400))
        self.screen.blit(ai, (500, 400))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x < 350:
                        return False
                    else:
                        return True

    def get_player(self):
        # Determine if the player is X or O
        self.screen.fill(self.WHITE)
        text = pygame.font.SysFont('comicsans', 100).render('Player is...', True, self.BLACK)
        # On the left have X and on the right have O separated by a line
        x = pygame.font.SysFont('comicsans', 100).render('X', True, self.RED)
        o = pygame.font.SysFont('comicsans', 100).render('O', True, self.YELLOW)
        pygame.draw.line(self.screen, self.BLACK, (350, 300), (350, 600), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 300), (700, 300), 5)
        self.screen.blit(text, (100, 100))
        self.screen.blit(x, (100, 400))
        self.screen.blit(o, (500, 400))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x < 350:
                        return 'X'
                    else:
                        return 'O'

    def get_AI_mode(self):
        # Determine if the AI is easy or hard
        self.screen.fill(self.WHITE)
        text = pygame.font.SysFont('comicsans', 50).render('AI Difficulty...', True, self.BLACK)
        # On the left have easy and on the right have hard separated by a line
        easy = pygame.font.SysFont('comicsans', 30).render('Easy', True, self.BLACK)
        medium = pygame.font.SysFont('comicsans', 30).render('Medium', True, self.BLACK)
        hard = pygame.font.SysFont('comicsans', 30).render('Hard', True, self.BLACK)
        pygame.draw.line(self.screen, self.BLACK, (350, 200), (350, 600), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 400), (700, 400), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 200), (700, 200), 5)
        self.screen.blit(text, (100, 100))
        self.screen.blit(easy, (100, 300))
        self.screen.blit(medium, (100, 450))
        self.screen.blit(hard, (500, 450))

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x < 350 and mouse_y < 400:
                        return 'Random'
                    elif mouse_x < 350 and mouse_y > 400:
                        return 'Depth3'
                    else:
                        return 'Depth5'

    def play_again(self):
        # Draw a play again screen
        self.screen.fill(self.WHITE)
        text = pygame.font.SysFont('comicsans', 100).render('Play Again?', True, self.BLACK)
        # On the left have yes and on the right have no separated by a line
        yes = pygame.font.SysFont('comicsans', 100).render('Yes', True, self.BLACK)
        no = pygame.font.SysFont('comicsans', 100).render('No', True, self.BLACK)
        pygame.draw.line(self.screen, self.BLACK, (350, 300), (350, 600), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 300), (700, 300), 5)
        self.screen.blit(text, (100, 100))
        self.screen.blit(yes, (100, 300))
        self.screen.blit(no, (400, 300))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 100 <= mouse_x <= 250 and 300 <= mouse_y <= 400:
                        return True
                    elif 400 <= mouse_x <= 550 and 300 <= mouse_y <= 400:
                        return False