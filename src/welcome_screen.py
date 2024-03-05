import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ultimate Battleship")

# Load the background image
background_image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_background.jpg')
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Define text properties
font = pygame.font.Font(None, 75)  # Increase font size for the title
prompt_font = pygame.font.Font(None, 50)  # Smaller font size for the prompt

# Render each line of text
line1_surface = font.render("Welcome to", True, (139, 142, 0))  # Yellow text
line2_surface = font.render("Ultimate Battleship", True, (139, 142, 0))  # Yellow text
prompt_surface = prompt_font.render("Press any key to continue", True, (255, 255, 255))  # White text for the prompt

# Position each line of text
line1_rect = line1_surface.get_rect(center=(screen_width / 2, screen_height / 6))
line2_rect = line2_surface.get_rect(center=(screen_width / 2, screen_height / 6 + 75))
prompt_rect = prompt_surface.get_rect(center=(screen_width / 2, screen_height - 100))  # Position the prompt at the bottom

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Check for any key press
            # Proceed to the next part of your game here
            print("Key pressed, continue to the next screen")  # Placeholder for actual game transition
            running = False  # Exit the welcome screen loop

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw each line of text
    screen.blit(line1_surface, line1_rect)
    screen.blit(line2_surface, line2_rect)
    screen.blit(prompt_surface, prompt_rect)  # Draw the prompt

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()