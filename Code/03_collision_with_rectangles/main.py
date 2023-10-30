import pygame
from sys import exit  # # We use exit from sys to quit the programm in the if statement itself

"""
1. To check if rectangles collided or not use : colliderect()
             eg: rect1.colliderect(rect2) 

2. If you want to play with mouse then you can use : collidepoint()
             eg: rect1.collidepoint((x,y))

* To get the mouse position there are 2 options:
  i. pygame.mouse 
  ii. event loop
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

        # to check if the mouse button is pressed by the user
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        # event loop to check if the mouse collides with the player box
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("Mouse on the player")

    #  ******************* Adding Frames *******************
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)

    # moving snail to left
    snail_rect.left -= 4
    if snail_rect.right <= 0: snail_rect.right = 800

    #  ******************* colliderect *******************
    """if player_rect.colliderect(snail_rect):
        print("Collision")"""

    #  ******************* collidepoint *******************
    mouse_pos = pygame.mouse.get_pos()  # getting mouse position
    """if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)
