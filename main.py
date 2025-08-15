import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(800, 600))  # Criando a surface
print("Setup End")

print("Loop start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            pygame.quit()  # End pygame
