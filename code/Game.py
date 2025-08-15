import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))  # Criando a surface

    def run(self, ):
        while True:
            menu = Menu(self.window)
            pass

        # Check for all events
        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:  # Close window
        #       pygame.quit()  # End pygame
