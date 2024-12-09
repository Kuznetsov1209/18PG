# Example file showing a circle moving on screen
import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, heigth = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    v = 100
    dt = 0
    # limits FPS to 60
    fps = 60

    while running:
        screen.fill("purple")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, "red", event.pos, 40)
                pygame.draw.circle(screen, "red", (event.pos[0], width - event.pos[1]), 40)
                pygame.draw.circle(screen, "red", (event.pos[1], heigth - event.pos[0]), 40)


        pygame.display.flip()


        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

pygame.quit()