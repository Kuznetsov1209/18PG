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

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= v * dt
        if keys[pygame.K_s]:
            player_pos.y += v * dt
        if keys[pygame.K_a]:
            player_pos.x -= v * dt
        if keys[pygame.K_d]:
            player_pos.x += v * dt

        # flip() the display to put your work on screen
        pygame.display.flip()


        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

pygame.quit()