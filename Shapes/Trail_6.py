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

# List to store the click counts
click_counts = []

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key
                click_counts.append(click_count)
                print(f"Stored click count: {click_count}")
                click_count = 0  # Reset the click counter

    # Draw the image
    screen.blit(image, (0, 0))

    # Draw the click count
    text_surface = font.render(f"Click count: {click_count}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))  # Position the text at (10, 10)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()