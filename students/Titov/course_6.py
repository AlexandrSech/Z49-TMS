import pygame
import random
import time
counter = 0
WIDTH = 1000    # ширина игрового окна
HEIGHT = 1000   # высота игрового окна
FPS = 30        # частота кадров в секунду
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
pygame.display.update()
# Цикл игры
running = True
#
while running:
    a = True
    for event in pygame.event.get():
        screen.fill((255, 255, 255))
        black = (0, 0, 0)
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('puk')
            prev_cords = ()
            while a:
                if pygame.MOUSEBUTTONUP and event.button == 1:
                    a = False
                    print(1)
                else:
                    print(event.pos)
                    prev_pos = []
                    prev_pos.append(event.pos[0])
                    prev_pos.append(event.pos[1])
                    if event.pos[0] != prev_pos and event.pos[1] != prev_pos:
                        pygame.draw.rect(screen, (0,0,0), (event.pos[0], event.pos[1], 5, 5))
                        pygame.display.update()
            '''screen.fill((255, 255, 255))
            counter += 1
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Вы нажали столько раз:' + str(counter), True,
                              (0, 0, 0))
            screen.blit(text1, (10, 50))
            pygame.display.update()
            print(event)'''

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            pygame.draw.line(screen, black,
                             [10, 30],
                             [290, 15], 3)
            pygame.draw.line(screen, black,
                             [10, 50],
                             [290, 35])
            pygame.draw.aaline(screen, black,
                               [10, 70],
                               [290, 55])
            pygame.draw.rect(screen, (0, 255, 255),
                             (20, 20, 50, 50))
            pygame.draw.rect(screen, (64, 128, 255),
                             (150, 20, 100, 75), 8)
            pygame.display.update()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)