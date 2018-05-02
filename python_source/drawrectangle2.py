import pygame

size = (700, 500)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode(size)
while(1):
    pygame.draw.rect(screen, GREEN, [50,50,100,100])