import pygame
import g_class
import time

WIDTH = 1000  # ширина игрового окна
HEIGHT = 1000 # высота игрового окна
FPS = 60 # частота кадров в секунду
counter = 0


pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

snake = g_class.Snake(screen, 4, (100, 100,), direction='right')

running = True
while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    snake.make_step()

    pygame.display.update()

    time.sleep(1)