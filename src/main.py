import pygame
import sys
from welcome_screen import WelcomeScreen
from asset_manager import AssetManager

def main():
    # Initialize Pygame and the mixer module
    pygame.init()
    pygame.mixer.init()

    # Set up the display
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ultimate Battleship")

    # Create the asset manager and welcome screen
    assets = AssetManager()
    welcome = WelcomeScreen(screen, assets)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game loop if ESC is pressed
                else:
                    welcome.handle_keypress(event.key)

        welcome.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
