import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()

# Constants
SNAKE_SIZE = 20
APPLE_SIZE = SNAKE_SIZE
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 15

# Directions
KEY = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font
FPS = 11
font = pygame.font.SysFont("Arial", 25)

# Clock
clock = pygame.time.Clock()

def draw_snake(snake_positions):
    for pos in snake_positions:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_apple(apple_position):
    pygame.draw.rect(screen, RED, pygame.Rect(apple_position[0], apple_position[1], APPLE_SIZE, APPLE_SIZE))

def display_score_and_time(score, elapsed_time):
    score_text = font.render(f"Score: {score}", True, WHITE)
    time_text = font.render(f"Time: {int(elapsed_time)}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))

def main():
    snake_positions = [(100, 100), (90, 100), (80, 100)]
    direction = (1, 0)  # Start moving to the right
    apple_position = (random.randint(0, (SCREEN_WIDTH // APPLE_SIZE) - 1) * APPLE_SIZE,
                      random.randint(0, (SCREEN_HEIGHT // APPLE_SIZE) - 1) * APPLE_SIZE)
    score = 0
    start_time = pygame.time.get_ticks()  # Get the starting time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = KEY["UP"]
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = KEY["DOWN"]
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = KEY["LEFT"]
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = KEY["RIGHT"]

        # Move the snake
        new_head = (snake_positions[0][0] + direction[0] * SNAKE_SIZE,
                    snake_positions[0][1] + direction[1] * SNAKE_SIZE)
        
        # Check for collision with apple
        if new_head == apple_position:
            snake_positions.insert(0, new_head)
            apple_position = (random.randint(0, (SCREEN_WIDTH // APPLE_SIZE) - 1) * APPLE_SIZE,
                              random.randint(0, (SCREEN_HEIGHT // APPLE_SIZE) - 1) * APPLE_SIZE)
            score += 1  # Increase score
        else:
            snake_positions.insert(0, new_head)
            snake_positions.pop()  # Remove the last segment of the snake

        # Check for collision with boundaries
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
            new_head in snake_positions[1:]):  # Check collision with self
            print("Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

        # Clear screen
        screen.fill(BLACK)

        # Draw everything
        draw_snake(snake_positions)
        draw_apple(apple_position)

        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds

        # Display score and time
        display_score_and_time(score, elapsed_time)

        # Refresh the display
        pygame.display.flip()

        # Control the speed of the game
        clock.tick(FPS)

if __name__ == "__main__":
    main()
