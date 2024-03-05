import pygame
from asset_manager import AssetManager

class WelcomeScreen:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.show_welcome = True

    def handle_keypress(self, key):
        if self.show_welcome:
            # Switch to showing instructions after any key press (except ESC)
            self.show_welcome = False

    def draw(self):
        # Draw the background
        self.screen.blit(self.assets.background_image, (0, 0))

        if self.show_welcome:
            # Draw the welcome text and prompt
            self.assets.draw_welcome(self.screen)
        else:
            # Draw the instruction text
            self.assets.draw_instructions(self.screen)