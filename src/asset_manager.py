import pygame
import os

import pygame
import os

class AssetManager:
    def __init__(self):
        # Initialize the asset manager and load the background image
        self.load_background_image()
        # Load the background music
        self.load_background_music()
        # Load the grid image
        self.load_grid_image()
        # Define text properties and render text
        self.define_text_properties()

    def load_background_image(self):
        background_image_path = self.get_asset_path('welcome_background.jpg')
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))

    def load_background_music(self):
        sound_path = self.get_asset_path('welcome_music.mp3')
        self.welcome_music = pygame.mixer.Sound(sound_path)
        self.welcome_music.play(-1)  # Play the music on loop

    def load_grid_image(self):
        grid_image_path = self.get_asset_path('Grid.jpg')  # Make sure to use the correct filename
        self.grid_image = pygame.image.load(grid_image_path)
        self.grid_image = pygame.transform.scale(self.grid_image, (1280, 720))  # Scale if needed

    def get_asset_path(self, filename):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', filename)

    def define_text_properties(self):
        self.font = pygame.font.Font(None, 75)  # Increase font size for the title
        self.prompt_font = pygame.font.Font(None, 50)  # Smaller font size for the prompt
        self.instruction_font = pygame.font.Font(None, 50)  # Smaller font size for the instructions

        self.welcome_line1 = self.font.render("Welcome to", True, (139, 142, 0))  # Yellow text
        self.welcome_line2 = self.font.render("Ultimate Battleship", True, (139, 142, 0))  # Yellow text
        self.prompt_surface = self.prompt_font.render("Press any key to continue or ESC to quit", True, (255, 255, 255))  # White text for the prompt

        self.instructions = [
            "Instructions:",
            "1. Place your ships on the grid.",
            "2. Take turns firing at the opponent's grid.",
            "3. First to sink all opponent's ships wins!",
            "Press any key to start the game or ESC to quit."
        ]

    def draw_welcome(self, screen):
        line1_rect = self.welcome_line1.get_rect(center=(1280 / 2, 720 / 6))
        line2_rect = self.welcome_line2.get_rect(center=(1280 / 2, 720 / 6 + 75))
        prompt_rect = self.prompt_surface.get_rect(center=(1280 / 2, 720 - 100))
        screen.blit(self.welcome_line1, line1_rect)
        screen.blit(self.welcome_line2, line2_rect)
        screen.blit(self.prompt_surface, prompt_rect)

    def draw_instructions(self, screen):
        for i, line in enumerate(self.instructions):
            instruction_surface = self.instruction_font.render(line, True, (255, 255, 255))
            screen.blit(instruction_surface, (1280 / 2 - instruction_surface.get_width() / 2, 720 / 3 + i * 50))
