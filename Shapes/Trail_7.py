import pygame

# Initialize Pygame
pygame.init()

# Load the image
image = pygame.image.load('img.png')  # Replace with your image file
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

# Variables to store the click counts
circle = 0
square = 0
triangle = 0
cross = 0

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
            if event.key == pygame.K_c:  # "c" key
                circle = click_count
                print(f"Stored click count in circle: {click_count}")
                click_count = 0  # Reset the click counter
            elif event.key == pygame.K_s:  # "s" key
                square = click_count
                print(f"Stored click count in square: {click_count}")
                click_count = 0  # Reset the click counter
            elif event.key == pygame.K_t:  # "t" key
                triangle = click_count
                print(f"Stored click count in triangle: {click_count}")
                click_count = 0  # Reset the click counter
            elif event.key == pygame.K_x:  # "x" key
                cross = click_count
                print(f"Stored click count in cross: {click_count}")
                click_count = 0  # Reset the click counter

    # Draw the image
    screen.blit(image, (0, 0))

    # Draw the click count
    text_surface = font.render(f"Click count: {click_count}", True, (0, 0, 0))
    screen.blit(text_surface, (0, 0))  # Position the text at (10, 10)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# Print the stored click counts
print("Stored click counts:")
print(f"Circle: {circle}")
print(f"Square: {square}")
print(f"Triangle: {triangle}")
print(f"Cross: {cross}")
total = (circle * 20) + (square * 15) + (triangle * 10) + (cross * 5)
print(f"total: {total}")