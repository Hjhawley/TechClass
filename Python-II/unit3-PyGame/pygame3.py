# 3. Handling Input
#
# Games often require interaction from the user. Pygame allows you to detect keyboard and mouse events.

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Handling Input")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Rectangle position
rect_x = 350
rect_y = 250

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handling keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= 5
    if keys[pygame.K_RIGHT]:
        rect_x += 5
    if keys[pygame.K_UP]:
        rect_y -= 5
    if keys[pygame.K_DOWN]:
        rect_y += 5

    # Fill the screen with white
    screen.fill(white)

    # Draw a blue rectangle at the new position
    pygame.draw.rect(screen, blue, (rect_x, rect_y, 100, 50))

    pygame.display.flip()

pygame.quit()
