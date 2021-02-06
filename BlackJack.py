import pygame, sys
from pygame.locals import *
from Card import *
from Deck import *

def game():
    '''
    This function runs all aspects of the game - including the display
    '''

    #rendered text
    text_one= TTF_Tusj50.render('BLACK JACK', 1, TITLECOLOR)
    player_tag = Lobster30.render('Player\'s Hand',1, RED)
    dealer_tag = Lobster30.render('Dealer\'s Hand',1, RED)
    hit_text = Arial30.render('HIT!',1,BLACK)
    stand_text = Arial30.render('STAND!',1,BLACK)
    play_again_text = Arial20.render('PLAY AGAIN?',1,BLACK)
    ppv_text = Arial40.render(str(player_points),1,BLACK)
    dpv_text = Arial40.render(str(dealer_points),1,BLACK)
        

    #Displayed Text
    screen.blit(text_one,(250,10))
    screen.blit(player_tag,(10, 350))
    screen.blit(dealer_tag,(10, 100))
    pygame.draw.rect(screen, BUTTONS, draw_button, border_radius = 5)
    pygame.draw.rect(screen, BUTTONS, stand_button, border_radius = 5)
    screen.blit(hit_text, (85,410))
    screen.blit(stand_text, (55,485))
    screen.blit(dpv_text,(650,100))
    screen.blit(ppv_text,(650,350))
    if gamestate == 2:
        pygame.draw.rect(screen, BUTTONS, play_again, border_radius = 5)
        screen.blit(play_again_text,(630,25))
    
    px = 210
    dx = 210
    for i in p_hand:
        i.draw(screen,px,350)
        px += 30
    for i in d_hand:
        i.draw(screen,dx,100)
        dx += 30

def dealer_turn():
    '''
    this function plays the entire dealer turn
    updates the display with correct values
    '''
    global dealer_points
    d_hand[0].flip()
    dealer_points = point_calc(d_hand)
    while dealer_points < 17 and dealer_points < 22:
        d_hand.append(deck.draw())
        dealer_points = point_calc(d_hand)
    dpv_text = Arial40.render(str(dealer_points),1,BLACK)

def point_calc(hand):
    '''
    caclulates the current total points of the hand
    changes ACE's from 11 to 1 point if point total over 21
    '''
    
    points = 0
    for c in hand:
        points += c.point_value
    i = 0
    while points > 21 and i < len(hand):
        if hand[i].point_value == 11:
            hand[i].point_value = 1
            points = 0
            for c in hand:
                points += c.point_value
        i += 1
    return points
    
pygame.init()
screen = pygame.display.set_mode((800,600))

#Fonts
Arial40 = pygame.font.SysFont("Arial",40)
Arial30 = pygame.font.SysFont("Arial",30)
Arial20 = pygame.font.SysFont("Arial",20)
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
stand_button = Rect(50, 475, 120, 50)
play_again = Rect(625, 10, 135, 50) 

#Deck and Hands
deck = Deck()
p_hand = []
d_hand = []

for x in range (2):
    p_hand.append(deck.draw())
    d_hand.append(deck.draw())
d_hand[0].flip()

player_points = point_calc(p_hand)
dealer_points = point_calc(d_hand) - d_hand[0].point_value
end = True
gamestate = 1
while end:
    screen.fill((TABLECOLOR))

    if gamestate == 1 or gamestate == 2:
        game()
    print(gamestate)
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
                        player_points = point_calc(p_hand)
                    if stand_button.collidepoint(event.pos):
                        gamestate = 2
                        dealer_turn()
                    if play_again.collidepoint(event.pos):
                        gamestate = 1
                        deck = Deck()
                        p_hand = []
                        d_hand = []

                        for x in range (2):
                            p_hand.append(deck.draw())
                            d_hand.append(deck.draw())
                        d_hand[0].flip()

                        player_points = point_calc(p_hand)
                        dealer_points = point_calc(d_hand) - d_hand[0].point_value
