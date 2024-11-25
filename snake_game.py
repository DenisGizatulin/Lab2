import pygame


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

