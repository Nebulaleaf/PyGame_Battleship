import pygame
import os

class AssetManager:
    def __init__(self):
        # Load the background image
        background_image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_background.jpg')
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))

        # Load the background music
        sound_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'welcome_music.mp3')
        self.welcome_music = pygame.mixer.Sound(sound_path)
        self.welcome_music.play(-1)  # Play the music on loop

        # Define text properties
        self.font = pygame.font.Font(None, 75)  # Increase font size for the title
        self.prompt_font = pygame.font.Font(None, 50)  # Smaller font size for the prompt
        self.instruction_font = pygame.font.Font(None, 50)  # Smaller font size for the instructions

        # Render each line of text
        self.welcome_line1 = self.font.render("Welcome to", True, (139, 142, 0))  # Yellow text
        self.welcome_line2 = self.font.render("Ultimate Battleship", True, (139, 142, 0))  # Yellow text
        self.prompt_surface = self.prompt_font.render("Press any key to continue or ESC to quit", True, (255, 255, 255))  # White text for the prompt

        # Instruction text (split into multiple lines if necessary)
        self.instructions = [
            "Instructions:",
            "1. Place your ships on the grid.",
            "2. Take turns firing at the opponent's grid.",
            "3. First to sink all opponent's ships wins!",
            "Press any key to start the game or ESC to quit."
        ]

    def draw_welcome(self, screen):
        # Position each line of text
        line1_rect = self.welcome_line1.get_rect(center=(1280 / 2, 720 / 6))
        line2_rect = self.welcome_line2.get_rect(center=(1280 / 2, 720 / 6 + 75))
        prompt_rect = self.prompt_surface.get_rect(center=(1280 / 2, 720 - 100))  # Position the prompt at the bottom

        # Draw the welcome text
        screen.blit(self.welcome_line1, line1_rect)
        screen.blit(self.welcome_line2, line2_rect)
        # Draw the "Press any key to continue" prompt
        screen.blit(self.prompt_surface, prompt_rect)

    def draw_instructions(self, screen):
        # Draw the instruction text
        for i, line in enumerate(self.instructions):
            instruction_surface = self.instruction_font.render(line, True, (255, 255, 255))  # White text for instructions
            screen.blit(instruction_surface, (1280 / 2 - instruction_surface.get_width() / 2, 720 / 3 + i * 50))

print("hello world")