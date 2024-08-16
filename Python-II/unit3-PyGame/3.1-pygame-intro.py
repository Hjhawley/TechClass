# Introduction to Pygame
# Pygame is a popular Python library used for creating video games. 
# It provides functionality for rendering graphics, handling input from the keyboard or mouse, playing sound, and more.

# Before starting, you need to install Pygame if you haven't already.
# You can install it using pip:
# pip install pygame

# Import the Pygame module.
import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("My First Pygame Window")

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
