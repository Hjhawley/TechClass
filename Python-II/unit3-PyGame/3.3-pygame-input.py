# Handling User Input in Pygame

# Most games require interaction from the user, such as moving a character or selecting options.
# Pygame allows you to detect and respond to keyboard and mouse events.

import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
# We create an 800x600 pixel window where our game will be displayed.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Handling Input")

# Define Colors
# As before, colors are defined using RGB tuples.
white = (255, 255, 255)  # White color for the background
teal = (0, 128, 128)     # Teal color for the rectangle

# Initialize Rectangle Position
# We start by defining the initial position of the rectangle on the screen.
rect_x = 350  # The x-coordinate of the rectangle's top-left corner
rect_y = 250  # The y-coordinate of the rectangle's top-left corner

# Run the game loop
# The game loop handles events and updates the display continuously.
running = True
while running:
    # Event handling loop
    # Pygame captures all events (like key presses or mouse clicks) in the event queue.
    for event in pygame.event.get():
        # Check if the close button is clicked
        if event.type == pygame.QUIT:
            running = False

    # Handling Keyboard Input
    # Pygame provides the key.get_pressed() method, which returns a dictionary of all keyboard keys and their current state (pressed or not).
    keys = pygame.key.get_pressed()
    
    # Move the rectangle left if the left arrow key is pressed
    if keys[pygame.K_LEFT]:
        rect_x -= .1  # Move left by decreasing the x-coordinate by .1 pixels
        # We pick a very small number because it will move by that amount every single frame the key is being held
        
    # Move the rectangle right if the right arrow key is pressed
    if keys[pygame.K_RIGHT]:
        rect_x += .1  # Move right by increasing the x-coordinate
        
    # Move the rectangle up if the up arrow key is pressed
    if keys[pygame.K_UP]:
        rect_y -= .1  # Move up by decreasing the y-coordinate
        
    # Move the rectangle down if the down arrow key is pressed
    if keys[pygame.K_DOWN]:
        rect_y += .1  # Move down by increasing the y-coordinate

    # Fill the screen with white
    # Before drawing anything, we clear the screen by filling it with a background color.
    screen.fill(white)

    # Draw a teal Rectangle at the New Position
    # After handling the input, we draw the rectangle at its updated position.
    pygame.draw.rect(screen, teal, (rect_x, rect_y, 100, 50))

    # Update the display
    # Finally, we update the display to reflect the changes made in this frame.
    pygame.display.flip()

# Quit Pygame
# When the game loop ends, we clean up by quitting Pygame.
pygame.quit()
