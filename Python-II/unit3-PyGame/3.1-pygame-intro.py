# Intro to Pygame

# Pygame is a popular Python library that is used for creating video games.
# It provides various functionalities such as rendering graphics, handling input from the keyboard or mouse, playing sound, and more.

# Before you can use Pygame, you need to install it. 
# You can install Pygame using the pip package manager:
# pip install pygame

# Import the Pygame module to use its functionalities.
import pygame

# Initialize Pygame
# This function initializes all the Pygame modules. 
# It's important to call this before using any Pygame features.
pygame.init()

# Set up the display window
# Pygame allows you to create a window where your game will be displayed.
# Here, we define the width and height of the window in pixels.
screen_width = 800   # The width of the window
screen_height = 600  # The height of the window
# The display.set_mode function initializes a window or screen for display.
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
# This sets the caption at the top of the window, which is useful for identifying your game.
pygame.display.set_caption("My First Pygame Window")

# Run the game loop
# The game loop is where the main events of the game occur.
# It typically includes checking for user input, updating game state, and rendering the graphics.

# We start by setting a variable to control whether the game is running.
running = True
while running:
    # Handle events
    # Pygame handles events (such as user input) through an event queue.
    # We loop through all events currently in the queue.
    for event in pygame.event.get():
        # Check if the user wants to close the window
        if event.type == pygame.QUIT:
            # If the event is of type QUIT (e.g., clicking the close button),
            # we set running to False, which will exit the loop and end the game.
            running = False

    # Fill the screen with a color
    # The screen.fill function fills the entire window with a specific color.
    # Colors are defined using RGB values. Here, (0, 0, 0) corresponds to black.
    screen.fill((0, 0, 0))

    # Update the display
    # The display.flip function updates the contents of the entire display.
    # It's necessary to call this to make any changes visible on the screen.
    pygame.display.flip()

# Quit Pygame
# Once the game loop is over, we call pygame.quit() to clean up and close the game properly.
pygame.quit()
