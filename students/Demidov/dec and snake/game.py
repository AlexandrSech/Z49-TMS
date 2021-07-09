from typing import Counter
import pygame
import time

WIDTH = 1080  # ширина игрового окна
HEIGHT = 720 # высота игрового окна
FPS = 60 # частота кадров в секунду
counter = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            prev_pos = event.pos
            while mouse_down:
                for m_event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        mouse_down = False
                    else:
                        if event.pos != prev_pos:
                            pygame.draw.rect(screen, (0, 0, 0), (event.pos[0], event.pos[1], 5, 5))
                            pygame.display.update()
                            prev_pos = event.pos



            '''
            screen.fill((0, 0, 0))
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('push me {}'.format(counter), True, 
                             (180, 0, 0))
            counter += 1
            screen.blit(text1, (50, 50))
            '''
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            screen.fill((255, 255, 255))
            pygame.display.update()