import pygame
import time
import Game_class


WIDTH = 980    # ширина игрового окна
HEIGHT = 600   # высота игрового окна
FPS = 30        # частота кадров в секунду


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first python")
clock = pygame.time.Clock()

snake = Game_class.Snake(screen, 4, (100, 100,))


# Цикл игры
running = True
while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    snake.draw()

    # pygame.display.update()

    time.sleep(1)