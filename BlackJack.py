import pygame, sys
from pygame.locals import *
from Card import *
from Deck import *

def game():
    px = 210
    dx = 210
    for i in p_hand:
        i.draw(screen,px,350)
        px += 30
    for i in d_hand:
        i.draw(screen,dx,100)
        dx += 30
    
pygame.init()
screen = pygame.display.set_mode((800,600))

deck = Deck()
p_hand = []
d_hand = []

for x in range (2):
    p_hand.append(deck.draw())
    d_hand.append(deck.draw())
d_hand[0].flip()
    
end = True
while end:
    screen.fill((255,255,255))

    game()

    
    pygame.display.update()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
