import pygame

# تنظیمات اولیه
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Open World FPS")

# مختصات بازیکن
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# حلقه اصلی بازی
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت بازیکن
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= player_speed  # بالا
    if keys[pygame.K_s]: player_y += player_speed  # پایین
    if keys[pygame.K_a]: player_x -= player_speed  # چپ
    if keys[pygame.K_d]: player_x += player_speed  # راست

    # رسم صفحه
    screen.fill((0, 0, 0))  # پس‌زمینه مشکی
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 10)  # بازیکن
    pygame.display.flip()

pygame.quit()
