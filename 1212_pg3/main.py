# Example file showing a circle moving on screen
import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_sizze = 30

    def render(self, screen):
        pass


def main():
    pygame.init()
    size = width, heigth = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board(5, 7)
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
        screen.fill("black")
        board.render(screen)
        pygame.display.flip()

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000


pygame.quit()

if __name__ == '__main__':
    main()
