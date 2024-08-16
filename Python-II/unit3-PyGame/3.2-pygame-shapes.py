# Drawing Shapes in Pygame

# Pygame provides various functions to draw basic shapes like rectangles, circles, lines, and more.
# In this lesson, we'll see how to draw a rectangle, circle, and line using Pygame.

import pygame

# Initialize Pygame
# As always, we start by initializing Pygame.
pygame.init()

# Set up the display window
# We define the dimensions of the window where our shapes will be drawn.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes with Pygame")

# Define Colors
# Colors in Pygame are represented by tuples of three values, corresponding to the Red, Green, and Blue (RGB) color channels.
white = (255, 255, 255)  # White color (maximum values for all three channels)
red = (255, 0, 0)        # Red color (maximum red, no green or blue)
green = (0, 255, 0)       # Green color (maximum green, no red or blue)
blue = (0, 0, 255)        # Blue color (maximum blue, no red or green)

# Run the game loop
# The game loop is where we handle events and update the display.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is clicked, exit the loop
            running = False

    # Fill the screen with white
    # Before drawing any shapes, we usually clear the screen by filling it with a solid color.
    screen.fill(white)

    # Draw a Red Rectangle
    # The draw.rect function draws a rectangle on the screen.
    # It takes the surface to draw on, the color, and a rectangle defined by (x, y, width, height).
    pygame.draw.rect(screen, red, (150, 100, 200, 150))

    # Draw a Green Circle
    # The draw.circle function draws a circle on the screen.
    # It takes the surface to draw on, the color, the center position (x, y), and the radius of the circle.
    pygame.draw.circle(screen, green, (400, 300), 75)

    # Draw a Blue Line
    # The draw.line function draws a straight line between two points.
    # It takes the surface to draw on, the color, the start position (x1, y1), the end position (x2, y2), and the line thickness.
    pygame.draw.line(screen, blue, (100, 500), (700, 500), 5)

    # Update the display
    # After drawing the shapes, we update the display to reflect the changes.
    pygame.display.flip()

# Quit Pygame
# When the game loop ends, we clean up by quitting Pygame.
pygame.quit()
