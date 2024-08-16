# 4. Adding Sound
#
# Pygame also supports playing sound effects and music.
# Here’s how you can add sound to your game.

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adding Sound")

# Load a sound effect
sound_effect = pygame.mixer.Sound('sound_effect.wav')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_effect.play()

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
