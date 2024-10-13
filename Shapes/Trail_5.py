import pygame

# Initialize Pygame
pygame.init()

# Load the image
image = pygame.image.load('Shapes.png')  # Replace with your image file
image_width, image_height = image.get_size()

# Set up the window dimensions
window_width = image_width
window_height = image_height
screen = pygame.display.set_mode((window_width, window_height))

# Set up the title of the window
pygame.display.set_caption("Click Counter")

# Initialize the click counter
click_count = 0

# Font for displaying the click count
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                click_count += 1

    # Draw the image
    screen.blit(image, (0, 0))

    # Draw the click count
    text_surface = font.render(f"Click count: {click_count}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))  # Position the text at (10, 10)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

print("Click count:", click_count)