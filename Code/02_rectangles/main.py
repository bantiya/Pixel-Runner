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

test_font = pygame.font.Font("../../font/Pixeltype.ttf", 50)

#  ******************* Adding surfaces *******************
sky_surface = pygame.image.load("../../graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("../../graphics/ground.png").convert_alpha()
text_surface = test_font.render("My Game", False, "Black").convert_alpha()
snail_surface = pygame.image.load("../../graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("../../graphics/Player/player_walk_1.png").convert_alpha()

#  ******************* Creating rectangle *******************
player_rect = player_surface.get_rect(midbottom=(80, 300))
snail_rect = snail_surface.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #  ******************* Adding Frames *******************
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)

    # moving snail to left
    snail_rect.left -= 4
    if snail_rect.right <= 0: snail_rect.right = 800

    pygame.display.update()
    clock.tick(60)
