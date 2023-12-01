import math
from random import randint
import pygame
from sys import exit  # # We use exit from sys to quit the programm in the if statement itself

"""
We use timer for enemy Spawn c 
"""


def display_score():
    current_time = math.floor((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(str(current_time), False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def display_final_score(prev_score, top_score):
    final_score_surf = test_font.render("Your score: " + str(prev_score), False, (111, 196, 169))
    final_score_rect = final_score_surf.get_rect(center=(400, 80))
    top_score_surf = test_font.render("Top score: " + str(top_score), False, (111, 196, 169))
    top_score_rect = final_score_surf.get_rect(topright=(800, 8))
    screen.blit(final_score_surf, final_score_rect)
    screen.blit(top_score_surf, top_score_rect)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5  # move the obstacle by 5 pixel to left

            # draw surface to the screen according to the bottom of rectangle
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect):
                return True


def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


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
player_walk_1 = pygame.image.load("../../graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("../../graphics/Player/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("../../graphics/Player/jump.png").convert_alpha()

# Used for player walk animation
player_walk = [player_walk_1, player_walk_2]
player_index = 0  # Custom timer for player Walking

# Intro screen
player_stand = pygame.image.load("../../graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
game_title = test_font.render("Pixel Jumper", False, (111, 196, 169)).convert_alpha()
instruction = test_font.render("Press Space to start the game", False, (111, 196, 169)).convert_alpha()

# ********* Obstacles *********
# Snail
snail_frame_1 = pygame.image.load("../../graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("../../graphics/snail/snail2.png").convert_alpha()
# For animation of SNAIL
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame_1 = pygame.image.load("../../graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("../../graphics/Fly/Fly2.png").convert_alpha()
# For Animation of FLY
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_gravity = 0  # Gravity variable for the player to jump

#  ******************* Creating rectangle *******************
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
score_rect = text_surface.get_rect(center=(400, 50))

# Intro screen
player_stand_rect = player_stand.get_rect(center=(400, 200))
game_title_rect = game_title.get_rect(center=(400, 50))
instruction_rect = instruction.get_rect(center=(400, 350))

#  ******************* Calculating scores *******************
top_score = 0
final_score = 0

# Timer
"""
We add the + 1 to differentiate between different types of events in your game.
"""
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # quit the while loop if the game is exited

        if game_active:  # Check the game state
            # Allowing player to jump only if the player is on ground
            if player_rect.bottom == 300:
                if event.type == pygame.MOUSEBUTTONDOWN:  # Jump if mouse button is pressed
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20

                if event.type == pygame.KEYDOWN:  # Jump if pressed SPACE
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20

            # if USEREVENT is triggered
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 200)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]


        else:
            # Check if player pressed Space to restart the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()  # update the start time to update the ticks for the score

    if game_active:
        #  ******************* Adding Frames *******************
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        final_score = display_score()
        if final_score > top_score: top_score = final_score

        # Player Setting
        player_gravity += 1  # player gravity set to increase
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:  # Setting the floor for the player
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # check collisions
        if collisions(obstacle_rect_list):
            game_active = False

    else:
        obstacle_rect_list.clear()  # clearing the list
        screen.fill((94, 129, 162))  # turn the game down if player is out
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)
        screen.blit(instruction, instruction_rect)
        display_final_score(final_score, top_score)

    pygame.display.update()
    clock.tick(60)  # running at 60 fps
