import pygame, sys
from pygame.locals import *
from Card import *

pygame.init()
screen = pygame.display.set_mode((800,600))

card_one = Card("ACE","SPADES",11)
card_two = Card("TEN","CLUBS",2)

end = True
while end:
    screen.fill((255,255,255))
    card_one.draw(screen,250,350)
    card_two.draw(screen,290,350)
    pygame.display.update()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
