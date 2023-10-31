import pygame
from sys import exit  # # We use exit from sys to quit the programm in the if statement itself

"""
Keyboard input can be taken in two ways by : 
1. pygame.key
2. event loop
"""

pygame.init()

width = 800  # width of the game window
height = 400  # height of the game window
screen = pygame.display.set_mode((width, height))

# Change the title of the window
pygame.display.set_caption("Runner")

# Used to maintain the framerate of the game
clock = pygame.time.Clock()

test_font = pygame.font.Font("../../font/Pixeltype.ttf", 50)

#  ******************* Adding surfaces *******************
sky_surface = pygame.image.load("../../graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("../../graphics/ground.png").convert_alpha()
text_surface = test_font.render("My Game", False, (64,64,64)).convert_alpha()
snail_surface = pygame.image.load("../../graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("../../graphics/Player/player_walk_1.png").convert_alpha()

#  ******************* Creating rectangle *******************
player_rect = player_surface.get_rect(midbottom=(80, 300))
snail_rect = snail_surface.get_rect(midbottom=(80, 300))
score_rect = text_surface.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        """
        if you want to use event loop there are 2 steps
        Step 1: check if any button was pressed
        Step 2: Work with a Specific key
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Jump")

    #  ******************* Adding Frames *******************
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(player_surface, player_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(text_surface, score_rect)

    # moving snail to left
    snail_rect.left -= 4
    if snail_rect.right <= 0: snail_rect.right = 800
    screen.blit(snail_surface, snail_rect)

    """ #  ******************* Using pygame.key ******************* 
    keys = pygame.key.get_pressed()  # this returns a tuple of buttons in there current state
    if keys[pygame.K_SPACE]:
        print("Jump")"""

    pygame.display.update()
    clock.tick(60)
