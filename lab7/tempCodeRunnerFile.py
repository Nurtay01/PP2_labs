import pygame
import datetime

pygame.init()

# Load Mickey Mouse image
mickey_img = pygame.image.load("lab7/images/imgonline-com-ua-Resize-wVS1bFOHascFP85r.jpg")
mickey_rect = mickey_img.get_rect(center=(200, 200))

# Set up display
W, H = 400, 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Clock")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get current time
    current_time = datetime.datetime.now()
    minute = current_time.minute
    second = current_time.second

    # Rotate Mickey's hands
    minute_hand = pygame.transform.rotate(mickey_img, -(minute * 6))
    second_hand = pygame.transform.rotate(mickey_img, -(second * 6))

    # Clear the screen
    sc.fill((255, 255, 255))

    # Blit Mickey's hands onto the screen
    sc.blit(minute_hand, mickey_rect)
    sc.blit(second_hand, mickey_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(1000)  # Update every second

pygame.quit()
