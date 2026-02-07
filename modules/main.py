# from modul import say_hello, x

# say_hello()
# x()


# import time 
# print("start")
# time.sleep(10)
# print("stop")

import pygame
import sys

# Ініціалізація
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя перша гра 🎮")

# Кольори
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

# Гравець
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 5

clock = pygame.time.Clock()

# Головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # Малювання
    screen.fill(WHITE)
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_size, player_size)
    )

    pygame.display.flip()
    clock.tick(60)