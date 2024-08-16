# Drawing Basic Shapes in PyGame

# Pygame provides various functions to draw shapes like rectangles, circles, and lines.

import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes with Pygame")

# Colors (R, G, B)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw a red rectangle
    pygame.draw.rect(screen, red, (150, 100, 200, 150))

    # Draw a green circle
    pygame.draw.circle(screen, green, (400, 300), 75)

    # Draw a blue line
    pygame.draw.line(screen, blue, (100, 500), (700, 500), 5)

    # Update the display
    pygame.display.flip()

pygame.quit()
