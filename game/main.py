import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Размер окна
width = 1000
height = 600

# Цвета
bezh = (233, 229, 206)
black = (40, 113, 62)
red = (52, 129, 184)

# Инициализация окна игры
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Фиксированное количество кадров в секунду
clock = pygame.time.Clock()

# Размер змейки
snake_block = 25

# Скорость змейки
snake_speed = 5.5

# Шрифты
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


# Функция для отображения текущего счета
def our_score(score):
    value = score_font.render("Apples: " + str(score), True, black)
    game_display.blit(value, [0, 0])


# Отображение змейки на экране
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])


# Отображение сообщения о проигрыше
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])


# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    # Изначальное положение змейки
    x1 = width / 2
    y1 = height / 2

    # Изменение координат змейки
    x1_change = 0
    y1_change = 0

    # Создание тела змейки
    snake_list = []
    length_of_snake = 1

    # Создание позиции еды
    foodx = round(random.randrange(0, width - snake_block) / float(snake_block)) * snake_block
    foody = round(random.randrange(0, height - snake_block) / float(snake_block)) * snake_block

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("Game Over! Press Q", red)
            our_score(length_of_snake - 1)
            pygame.display.update()

            # Закрытие игры или продолжение
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Движение змейки
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

        # Если змейка выходит за границы окна - игра завершается
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(bezh)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []

        # Добавление изменения координат головы змейки
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Если змейка съела еду, увеличиваем длину змейки и создаем новую позицию еды
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-2]:
            if x == snake_head:
                game_close = True

        # Отображение змейки и текущего счета
        our_snake(snake_block, snake_list)
        our_score(length_of_snake - 1)

        pygame.display.update()

        # Если змейка съела еду, увеличиваем длину змейки и создаем новую позицию еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / float(snake_block)) * snake_block
            foody = round(random.randrange(0, height - snake_block) / float(snake_block)) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


# Запуск игры
game_loop()