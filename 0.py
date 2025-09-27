import pygame

#setting up pygame
pygame.init()
#setting up display
screen = pygame.display.set_mode((800, 600))
#setting up clock
clock = pygame.time.Clock()
#setting up font
font = pygame.font.Font('comic sans', 36)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    