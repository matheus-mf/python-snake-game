import random

import pygame

pygame.init()

blue = (50, 100, 213)
orange = (205, 102, 0)
green = (0, 255, 0)
yalow = (255, 255, 102)

dimensions = (600, 600)

position_snake_x = 300
position_snake_y = 300

dimension = 20

snake = [[position_snake_x, position_snake_y]]

delta_x = 0
delta_y = 0

position_food_x = round(random.randrange(0, 600 - dimension) / 20) * 20
position_food_y = round(random.randrange(0, 600 - dimension) / 20) * 20

text_font = pygame.font.SysFont("hack", 35)

screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption('My snake game')

screen.fill(blue)

clock = pygame.time.Clock()


def draw_snake(snake):
    screen.fill(blue)
    for unit in snake:
        pygame.draw.rect(screen, orange, [unit[0], unit[1], dimension, dimension])


def position_food_new_place():
    return round(random.randrange(0, 600 - dimension) / 20) * 20, round(random.randrange(0, 600 - dimension) / 20) * 20


def game_over():
    raise Exception


def move_snake(delta_x, delta_y, snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -dimension
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = dimension
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -dimension
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = dimension

    new_position_snake_x = snake[-1][0] + delta_x
    new_position_snake_y = snake[-1][1] + delta_y

    snake.append([new_position_snake_x, new_position_snake_y])

    del snake[0]

    return delta_x, delta_y, snake


def checks_food(delta_x, delta_y, position_food_x, position_food_y, snake):
    head = snake[-1]

    new_position_snake_x = head[0] + delta_x
    new_position_snake_y = head[1] + delta_y

    if head[0] == position_food_x and head[1] == position_food_y:
        snake.append([new_position_snake_x, new_position_snake_y])
        position_food_x, position_food_y = position_food_new_place()

    pygame.draw.rect(screen, green, [position_food_x, position_food_y, dimension, dimension])

    return position_food_x, position_food_y, snake


def checks_wall(snake):
    head = snake[-1]
    position_snake_x = head[0]
    position_snake_y = head[1]

    if position_snake_x not in range(600) or position_snake_y not in range(600):
        game_over()


def checks_if_snake_struck(snake):
    head = snake[-1]

    body = snake.copy()
    del body[-1]

    for x, y in body:
        if x == head[0] and y == head[1]:
            game_over()


def update_score(snake):
    pts = str(len(snake) - 1)
    score = text_font.render("Pontuação: " + pts, True, yalow)
    screen.blit(score, [0, 0])


while True:
    pygame.display.update()
    draw_snake(snake)

    delta_x, delta_y, snake = move_snake(delta_x, delta_y, snake)
    position_food_x, position_food_y, snake = checks_food(
        delta_x, delta_y, position_food_x, position_food_y, snake)

    checks_wall(snake)
    checks_if_snake_struck(snake)
    update_score(snake)

    clock.tick(10)
