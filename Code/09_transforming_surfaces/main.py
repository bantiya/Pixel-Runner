import math
import pygame
from sys import exit  # # We use exit from sys to quit the programm in the if statement itself

"""
pygame.transform is used to do different things with the objects like:
flip, scale, rotate, rotozoom, scale2x, smoothscale, ... , etc
"""


def display_score():
    current_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(str(current_time), False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def display_final_score(prev_score, top_score):
    final_score_surf = test_font.render("Your score: " + str(prev_score), False, (111,196,169))
    final_score_rect = final_score_surf.get_rect(center=(400, 80))
    top_score_surf = test_font.render("Top score: " + str(top_score), False, (111,196,169))
    top_score_rect = final_score_surf.get_rect(topright=(800, 8))
    screen.blit(final_score_surf, final_score_rect)
    screen.blit(top_score_surf, top_score_rect)


pygame.init()

width = 800  # width of the game window
height = 400  # height of the game window
screen = pygame.display.set_mode((width, height))

# Change the title of the window
pygame.display.set_caption("Runner")

# Used to maintain the framerate of the game
clock = pygame.time.Clock()

test_font = pygame.font.Font("../../font/Pixeltype.ttf", 50)

game_active = False  # Maintain game state
start_time = 0

#  ******************* Adding surfaces *******************
sky_surface = pygame.image.load("../../graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("../../graphics/ground.png").convert_alpha()
text_surface = test_font.render("My Game", False, (64, 64, 64)).convert_alpha()
snail_surface = pygame.image.load("../../graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("../../graphics/Player/player_walk_1.png").convert_alpha()

# Intro screen
player_stand = pygame.image.load("../../graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
game_title = test_font.render("Pixel Jumper", False, (111,196,169)).convert_alpha()
instruction = test_font.render("Press Space to start the game", False, (111,196,169)).convert_alpha()

player_gravity = 0  # Gravity variable for the player to jump

#  ******************* Creating rectangle *******************
player_rect = player_surface.get_rect(midbottom=(80, 300))
snail_rect = snail_surface.get_rect(midbottom=(80, 300))
score_rect = text_surface.get_rect(center=(400, 50))

# Intro screen
player_stand_rect = player_stand.get_rect(center=(400, 200))
game_title_rect = game_title.get_rect(center=(400, 50))
instruction_rect = instruction.get_rect(center=(400, 350))

#  ******************* Calculating scores *******************
top_score = 0
final_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # quit the while loop if the game is exited

        if game_active:  # Check the game state
            if player_rect.bottom == 300:  # Allowing player to jump only if the player is on ground
                if event.type == pygame.MOUSEBUTTONDOWN:  # Jump if mouse button is pressed
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20

                if event.type == pygame.KEYDOWN:  # Jump if pressed SPACE
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
        else:
            # Check if player pressed Space to restart the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.x = 800
                start_time = pygame.time.get_ticks()  # update the start time to update the ticks for the score

    if game_active:
        #  ******************* Adding Frames *******************
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        final_score = display_score()
        if final_score > top_score: top_score = final_score

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

        #  snail collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill((94, 129, 162))  # turn the game down if player is out
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)
        screen.blit(instruction, instruction_rect)
        display_final_score(final_score, top_score)

    pygame.display.update()
    clock.tick(60)  # running at 60 fps
