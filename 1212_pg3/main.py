# Example file showing a circle moving on screen
import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        self.screen = screen
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size,), self.board[y][x])

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 < x + 1 <= self.width and 0 < y + 1 <= self.height:
            return x, y

    def on_click(self, cell):
        print(f"Была выбрана ячейка {cell}")
        x, y = cell
        self.board[y][x] = int(not self.board[y][x])
        self.render(self.screen)


def main():
    pygame.init()
    size = width, heigth = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board(18, 12)
    board.set_view(100, 100, 15)
    running = True
    v = 100
    dt = 0
    # limits FPS to 60
    fps = 60

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill("black")
        board.render(screen)
        pygame.display.flip()

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000


pygame.quit()

if __name__ == '__main__':
    main()
