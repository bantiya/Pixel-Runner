import pygame
from sys import exit  # # We use exit from sys to quit the programm in the if statement itself

pygame.init()

width = 800  # width of the game window
height = 400  # height of the game window
screen = pygame.display.set_mode((width, height))

# Change the title of the window
pygame.display.set_caption("Runner")

# Used to maintain the framerate of the game
clock = pygame.time.Clock()

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# added convert alpha so that the image is converted into something that pygame can easily work with
"""
pygame has 2 surface one static and other regular so we make regular surfaces like sky, ground, text, and snail
which are then loaded on the main screen
"""
#  ******************* Adding surfaces *******************
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
text_surface = test_font.render("My Game", False, "Black").convert_alpha()

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 800
print("Hola")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # We use exit from sys to quit the program in the if statement itself and not go in the while loop again

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(350,50))
    snail_x_pos -= 4

    if snail_x_pos == 0:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))

    pygame.display.update()
    clock.tick(60)  # signifies that the while loop should not run more that 60 times per sec
