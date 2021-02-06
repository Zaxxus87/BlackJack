import pygame, sys
from pygame.locals import *
from Card import *
from Deck import *

def game():

    #rendered text
    text_one= TTF_Tusj50.render('BLACK JACK', 1, TITLECOLOR)
    player_tag = Lobster30.render('Player\'s Hand',1, RED)
    dealer_tag = Lobster30.render('Dealer\'s Hand',1, RED)
    hit_text = Arial40.render('HIT!',1,BLACK)

    #Displayed Text
    screen.blit(text_one,(250,10))
    screen.blit(player_tag,(10, 350))
    screen.blit(dealer_tag,(10, 100))
    pygame.draw.rect(screen, BUTTONS, draw_button, border_radius = 5)
    screen.blit(hit_text, (75,400))
    
    
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

#Fonts
Arial40 = pygame.font.SysFont("Arial",40)
TTF_Tusj50 = pygame.font.Font(os.path.join('Fonts','FFF_Tusj.ttf'),50)
TTF_Tusj30 = pygame.font.Font(os.path.join('Fonts','FFF_Tusj.ttf'),30)
Lobster30 = pygame.font.Font(os.path.join('Fonts','Lobster.ttf'),30)

#Colors
TITLECOLOR = (175,150,220)
WHITE = (255,255,255)
TABLECOLOR = (53,101,77)
RED = (255,0,0)
BLACK = (10, 10, 10)
BUTTONS = (250,225,25)

#Buttons
draw_button = Rect(50, 400, 120, 50)

#Deck and Hands
deck = Deck()
p_hand = []
d_hand = []

for x in range (2):
    p_hand.append(deck.draw())
    d_hand.append(deck.draw())
d_hand[0].flip()
    
end = True
gamestate = 1
while end:
    screen.fill((TABLECOLOR))

    if gamestate == 1:
        game()

    
    pygame.display.update()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()

        if event.type == MOUSEBUTTONUP and event.button == 1:
                if gamestate == 1:
                    if draw_button.collidepoint(event.pos):
                        p_hand.append(deck.draw())
