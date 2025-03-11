import pygame
from world import draw_world

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Open World FPS")

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= player_speed
    if keys[pygame.K_s]: player_y += player_speed
    if keys[pygame.K_a]: player_x -= player_speed
    if keys[pygame.K_d]: player_x += player_speed

    screen.fill((0, 0, 0))  # پس‌زمینه
    draw_world(screen)      # رسم نقشه
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 10)  # بازیکن
    pygame.display.flip()

pygame.quit()
