import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
BALL_RADIUS = 25
BALL_DIAMETER = BALL_RADIUS * 2
BALL_SPEED = 20

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

# Initial position of the ball
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - BALL_SPEED, BALL_RADIUS)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + BALL_SPEED, SCREEN_HEIGHT - BALL_RADIUS)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - BALL_SPEED, BALL_RADIUS)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + BALL_SPEED, SCREEN_WIDTH - BALL_RADIUS)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Add a small delay
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
