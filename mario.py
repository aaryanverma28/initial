import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario - Python Edition")
clock = pygame.time.Clock()

# Colors
SKY_TOP = (107, 140, 255)
SKY_BOTTOM = (200, 220, 255)
BROWN = (139, 69, 19)
PLATFORM_TOP = (222, 184, 135)
GOLD = (255, 215, 0)
PLAYER_SHIRT = (255, 0, 0)
SKIN = (255, 224, 189)
ENEMY_COLOR = (0, 0, 0)

# Player
player = pygame.Rect(100, 300, 28, 32)
player_vel_y = 0
on_ground = False

# Camera
camera_x = 0

# Platforms
platforms = [
    pygame.Rect(0, 350, 800, 50),
    pygame.Rect(300, 300, 100, 20),
    pygame.Rect(500, 250, 100, 20),
    pygame.Rect(700, 200, 100, 20)
]

# Coins
coins = [
    pygame.Rect(320, 260, 10, 10),
    pygame.Rect(520, 210, 10, 10),
    pygame.Rect(720, 160, 10, 10)
]
coins_taken = [False] * len(coins)

# Enemies
enemies = [
    pygame.Rect(600, 320, 30, 30)
]

def draw_gradient(surface, top_color, bottom_color):
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = top_color[0] * (1 - ratio) + bottom_color[0] * ratio
        g = top_color[1] * (1 - ratio) + bottom_color[1] * ratio
        b = top_color[2] * (1 - ratio) + bottom_color[2] * ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, y), (WIDTH, y))

def draw_player():
    px = player.x - camera_x
    py = player.y
    pygame.draw.rect(screen, PLAYER_SHIRT, (px, py + 8, player.width, player.height - 8))
    pygame.draw.rect(screen, SKIN, (px + 6, py, 16, 16))
    pygame.draw.rect(screen, (177, 18, 42), (px + 4, py - 6, 20, 8))
    pygame.draw.rect(screen, (0, 0, 255), (px + 4, py + player.height - 6, 10, 6))
    pygame.draw.rect(screen, (0, 0, 255), (px + player.width - 14, py + player.height - 6, 10, 6))

def game_loop():
    global player_vel_y, on_ground, camera_x
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        if keys[pygame.K_SPACE] and on_ground:
            player_vel_y = -12
            on_ground = False
        player_vel_y += 0.5
        player.y += player_vel_y
        on_ground = False
        for plat in platforms:
            if player.colliderect(plat) and player_vel_y >= 0:
                player.bottom = plat.top
                player_vel_y = 0
                on_ground = True
        camera_x = player.x - WIDTH // 2
        screen.fill((0, 0, 0))
        draw_gradient(screen, SKY_TOP, SKY_BOTTOM)
        for plat in platforms:
            pygame.draw.rect(screen, PLATFORM_TOP, (plat.x - camera_x, plat.y, plat.width, plat.height))
        for i, coin in enumerate(coins):
            if not coins_taken[i] and player.colliderect(coin):
                coins_taken[i] = True
            if not coins_taken[i]:
                pygame.draw.circle(screen, GOLD, (coin.x - camera_x + 5, coin.y + 5), 5)
        for enemy in enemies:
            pygame.draw.rect(screen, ENEMY_COLOR, (enemy.x - camera_x, enemy.y, enemy.width, enemy.height))
        draw_player()
        pygame.display.flip()
        clock.tick(60)

game_loop()
