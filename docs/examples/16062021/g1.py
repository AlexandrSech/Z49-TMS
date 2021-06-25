import pygame
import time

WIDTH = 1024    # ширина игрового окна
HEIGHT = 768    # высота игрового окна
FPS = 30        # частота кадров в секунду


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

counter = 0
# Цикл игры
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
                    if m_event.type == pygame.MOUSEBUTTONUP and m_event.button == 1:
                        mouse_down = False
                    if m_event.pos != prev_pos:
                        pygame.draw.rect(screen, (0, 0, 0), (prev_pos[0], prev_pos[1], 5, 5))
                        pygame.display.update()
                        prev_pos = m_event.pos



            '''screen.fill((0, 0, 0))
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('push me {}'.format(counter), True,
                              (180, 0, 0))
            counter += 1
            screen.blit(text1, (50, 50))'''
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            screen.fill((255, 255, 255))
            # pygame.draw.rect(screen, (255, 255, 255), (event.pos[0], event.pos[1], 100, 75))
            pygame.display.update()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)




