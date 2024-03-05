import pygame
import sys
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound effects

# Set up the display
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ultimate Battleship")

# Load the background image
background_image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_background.jpg')
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load the background music
sound_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_music.mp3')
welcome_music = pygame.mixer.Sound(sound_path)
welcome_music.play(-1)  # Play the music on loop

# Define text properties
font = pygame.font.Font(None, 75)  # Increase font size for the title
prompt_font = pygame.font.Font(None, 50)  # Smaller font size for the prompt
instruction_font = pygame.font.Font(None, 35)  # Smaller font size for the instructions

# Render each line of text
welcome_line1 = font.render("Welcome to", True, (139, 142, 0))  # Yellow text
welcome_line2 = font.render("Ultimate Battleship", True, (139, 142, 0))  # Yellow text
prompt_surface = prompt_font.render("Press any key to continue", True, (255, 255, 255))  # White text for the prompt

# Instruction text (split into multiple lines if necessary)
instructions = [
    "Instructions:",
    "1. Place your ships on the grid.",
    "2. Take turns firing at the opponent's grid.",
    "3. First to sink all opponent's ships wins!",
    "Press any key to start the game."
]

# Position each line of text
line1_rect = welcome_line1.get_rect(center=(screen_width / 2, screen_height / 6))
line2_rect = welcome_line2.get_rect(center=(screen_width / 2, screen_height / 6 + 75))
prompt_rect = prompt_surface.get_rect(center=(screen_width / 2, screen_height - 100))  # Position the prompt at the bottom

# Welcome screen state
show_welcome = True # Set to True to display the welcome screen

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Exit the game loop if ESC is pressed
            elif show_welcome:
                # Switch to showing instructions after any key press (except ESC)
                show_welcome = False

    # Draw the background
    screen.blit(background_image, (0, 0))

    if show_welcome:
        # Draw the welcome text
        screen.blit(welcome_line1, line1_rect)
        screen.blit(welcome_line2, line2_rect)
        # Draw the "Press any key to continue" prompt
        screen.blit(prompt_surface, prompt_rect)
    else:
        # Draw the instruction text
        for i, line in enumerate(instructions):
            instruction_surface = instruction_font.render(line, True, (255, 255, 255))  # White text for instructions
            screen.blit(instruction_surface, (screen_width / 2 - instruction_surface.get_width() / 2, screen_height / 3 + i * 50))

    # Update the display
    pygame.display.flip()

# Stop the background music
welcome_music.stop()

# Quit Pygame
pygame.quit()
sys.exit()