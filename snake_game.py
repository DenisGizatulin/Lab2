import pygame
import time
import random

def Snake_game():
    snake_speed = 15

    # Размер окна
    window_x = 720
    window_y = 480

    # Определяем цвета
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Инициализируем Pygame
    pygame.init()

    # Инициализируем игровое окно
    pygame.display.set_caption('Змейка')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) контроллер
    fps = pygame.time.Clock()

    # Определяем позицию по умолчанию для змейки
    snake_position = [100, 50]

    # Определяем первые 4 блока змейки
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    # Позиция яблока
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True

    # Змейка по уцмолчанию двигается вправо
    direction = 'RIGHT'
    change_to = direction

    # Количество набранных очков
    score = 0
