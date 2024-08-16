# Text and Sound Effects in Pygame

# In addition to graphics and user input, Pygame supports playing sound effects and music.
# This lesson demonstrates how to load and play a sound effect in response to a user action.

import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
# We create an 800x600 pixel window where our game will be displayed.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adding Sound")

# Load a Sound Effect
# Pygame's mixer module is used to handle sounds and music.
# We use the Sound class to load a sound effect from a file. Make sure the file 'sound_effect.wav' is in the same directory as your script.
# Supported formats include WAV, MP3, OGG, and more.
sound_effect = pygame.mixer.Sound('sound_effect.mp3')

# Run the game loop
running = True
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is clicked, exit the loop
            running = False
        if event.type == pygame.KEYDOWN:
            # Check if the spacebar is pressed
            if event.key == pygame.K_SPACE:
                # Play the sound effect
                # When the spacebar is pressed, we play the loaded sound effect.
                sound_effect.play()

    # Fill the screen with white
    # This clears the screen to white before drawing anything new.
    screen.fill((255, 255, 255))

    # Update the display
    # Finally, we update the display to reflect any changes.
    pygame.display.flip()

# Quit Pygame
# When the game loop ends, we clean up by quitting Pygame.
pygame.quit()
