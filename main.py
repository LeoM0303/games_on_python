import pygame
import time
import random

# install PyGame
pygame.init()

#colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
purple = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# size of game windows
width = 600
height = 400

# window of game
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('snake')

#install time
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Fonts for text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function for displaying an invoice
def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    window.blit(value, [0, 0])

# Function for drawing a snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# main game
def gameLoop():
    game_over = False
    game_close = False

    # Initial coordinates of the snake
    x1 = width / 2
    y1 = height / 2

    # Change coordinates
    x1_change = 0
    y1_change = 0

    # Initial settings of the snake
    snake_list = []
    length_of_snake = 1

    # Food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(blue)
            message("You've lost! Press Q to exit or C to repeat", purple)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        pygame.draw.rect(window, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# end game
gameLoop()
