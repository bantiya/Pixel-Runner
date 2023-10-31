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
text_surface = test_font.render("My Game", False, (64,64,64)).convert_alpha()
snail_surface = pygame.image.load("../../graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("../../graphics/Player/player_walk_1.png").convert_alpha()
player_gravity = 0

#  ******************* Creating rectangle *******************
player_rect = player_surface.get_rect(midbottom=(80, 300))
snail_rect = snail_surface.get_rect(midbottom=(80, 300))
score_rect = text_surface.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if player_rect.bottom == 300:  # allowing player to jump only if the player is on ground
            if event.type == pygame.MOUSEBUTTONDOWN:  # Jump if mouse button is pressed
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:  # Jump if pressed SPACE
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

    #  ******************* Adding Frames *******************
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(text_surface, score_rect)

    # moving snail to left
    snail_rect.left -= 4
    if snail_rect.right <= 0: snail_rect.right = 800
    screen.blit(snail_surface, snail_rect)

    # Player Setting
    player_gravity += 1  # player gravity set to increase
    player_rect.bottom += player_gravity
    if player_rect.bottom >= 300:  # Setting the floor for the player
        player_rect.bottom = 300
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)
