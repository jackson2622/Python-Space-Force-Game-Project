import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
PLAYER_SIZE = 50
BULLET_SIZE = 10
ENEMY_SIZE = 50
SPEED = 5
INITIAL_ENEMY_SPAWN_RATE = 100  # Initial spawn rate
ENEMY_SPAWN_RATE_DECREMENT = 5  # Decrease spawn rate by this amount every 10 seconds
ENEMY_SPEED_INCREMENT = 0.5  # Increase enemy speed by this amount every 10 seconds

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the player
player = pygame.Rect(WIDTH / 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 0

# Set up the bullets
bullets = []

# Set up the enemies
enemies = [pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(-HEIGHT, 0), ENEMY_SIZE, ENEMY_SIZE) for _ in range(10)]

# Set up the score
score = 0

# Set up the frame counter
frame_counter = 0
enemy_spawn_rate = INITIAL_ENEMY_SPAWN_RATE
enemy_speed = SPEED

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx, player.top, BULLET_SIZE, BULLET_SIZE))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
    if keys[pygame.K_RIGHT]:
        player.x += SPEED

    # Move the bullets
    for bullet in bullets:
        bullet.y -= SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move the enemies
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        if enemy.colliderect(player):
            print("Game Over")
            print("Final Score:", score)
            pygame.quit()
            sys.exit()

    # Check for collisions between bullets and enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Spawn new enemies
    frame_counter += 1
    if frame_counter >= enemy_spawn_rate:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(-HEIGHT, 0), ENEMY_SIZE, ENEMY_SIZE))
        frame_counter = 0

    # Increase difficulty over time
    if frame_counter % (60 * 10) == 0:  # Every 10 seconds
        enemy_spawn_rate -= ENEMY_SPAWN_RATE_DECREMENT
        if enemy_spawn_rate < 20:  # Don't go below 20 frames
            enemy_spawn_rate = 20
        enemy_speed += ENEMY_SPEED_INCREMENT

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, GREEN, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
