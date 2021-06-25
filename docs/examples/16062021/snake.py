import pygame
import time
import game_classes

WIDTH = 980    # ширина игрового окна
HEIGHT = 600   # высота игрового окна
FPS = 30        # частота кадров в секунду


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first python")
clock = pygame.time.Clock()

snake = game_classes.Snake(screen, 4, (100, 100,))


'''
<Event(768-KeyDown {'unicode': '', 'key': 1073741905, 'mod': 4096, 'scancode': 81, 'window': None})>
<Event(768-KeyDown {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})>
<Event(768-KeyDown {'unicode': '', 'key': 1073741906, 'mod': 4096, 'scancode': 82, 'window': None})>
<Event(768-KeyDown {'unicode': '', 'key': 1073741904, 'mod': 4096, 'scancode': 80, 'window': None})>
'''

dirs = {
    1073741905: 'down',
    1073741903: 'right',
    1073741906: 'up',
    1073741904: 'left'
}

# Цикл игры
running = True
while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            snake.change_dir(dirs[event.key])


    snake.make_step()

    # pygame.display.update()

    time.sleep(0.1)
