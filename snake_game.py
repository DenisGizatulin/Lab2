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

    # Функция для отображения счёта
    def show_score(choice, color, font, size):

        # Создание объекта score_font
        score_font = pygame.font.SysFont(font, size)


        score_surface = score_font.render('Счёт : ' + str(score), True, color)

        # Создание четырёхугольника для счёта
        score_rect = score_surface.get_rect()

        # отображаем текст
        game_window.blit(score_surface, score_rect)

    # Функция конца игры
    def game_over():

        try:
            with open('highscore.txt', 'r') as f:
                current_highscore = int(f.read())
        except (FileNotFoundError, ValueError):
            current_highscore = 0  # Значение счёта по умолчанию

            # Сравнение нынешнего результата с максимальным
        if score > current_highscore:
            # Если нынешний результат больше, чем максимальный, то записываем нынешний результат в файл
            with open('highscore.txt', 'w') as f:
                f.write('%d' % score)

        my_font = pygame.font.SysFont('times new roman', 50)

        # Создаём текстовую поверхность, на которой будем отображать результат
        game_over_surface = my_font.render(
            'Вы набрали : ' + str(score) + ' очков', True, red)

        # Создаём четырёхугольник
        game_over_rect = game_over_surface.get_rect()

        # Указываем позицию текста
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # Это будет выводить текст на экран
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # Устанавливаем задержку перед выходом
        time.sleep(2)

        # Выключаем Pygame
        pygame.quit()

        # Выход из программы
        quit()