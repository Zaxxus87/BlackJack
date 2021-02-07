import pygame, sys
from pygame.locals import *
from Card import *
from Deck import *

def open_screen():
    '''
    This function run all aspects of the opening screen - including display 
    '''
    #rendered Text
    welcome_message = MS_Sans_Serif60.render('Welcome to BlackJack',1,BLACK)
    play_text = Arial40.render('PLAY', 1, BLACK)
    exit_text = Arial40.render('EXIT', 1, BLACK)

    #Display
    screen.fill((175,25,0))
    screen.blit(welcome_message,(150,200))
    pygame.draw.rect(screen, BUTTONS, play, border_radius = 5)
    pygame.draw.rect(screen, BUTTONS, game_exit, border_radius = 5)
    screen.blit(play_text, (350,260))
    screen.blit(exit_text, (350,335))
    
def game():
    '''
    This function runs all aspects of the game - including the display
    '''
    global player_points
    global win_message
    global gamestate
    #rendered text
    text_one= TTF_Tusj50.render('BLACK JACK', 1, TITLECOLOR)
    player_tag = Lobster30.render('Player\'s Hand',1, RED)
    dealer_tag = Lobster30.render('Dealer\'s Hand',1, RED)
    hit_text = Arial30.render('HIT!',1,BLACK)
    stand_text = Arial30.render('STAND!',1,BLACK)
    play_again_text = Arial20.render('PLAY AGAIN?',1,BLACK)
    ppv_text = Arial40.render(str(player_points),1,BLACK)
    dpv_text = Arial40.render(str(dealer_points),1,BLACK)
    quit_txt = Arial20.render('QUIT',1,BLACK)
    win_txt = Arial30.render(win_message,1,BLACK)
        

    #Display
    screen.fill((TABLECOLOR))
    pygame.draw.rect(screen, BUTTONS, quit_game, border_radius = 5)
    screen.blit(quit_txt,(50,25))
    screen.blit(text_one,(250,10))
    screen.blit(player_tag,(10, 350))
    screen.blit(dealer_tag,(10, 100))
    pygame.draw.rect(screen, BUTTONS, draw_button, border_radius = 5)
    pygame.draw.rect(screen, BUTTONS, stand_button, border_radius = 5)
    screen.blit(hit_text, (85,410))
    screen.blit(stand_text, (55,485))
    screen.blit(dpv_text,(650,100))
    screen.blit(ppv_text,(650,350))
    if gamestate == 2 or gamestate == 3:
        pygame.draw.rect(screen, BUTTONS, play_again, border_radius = 5)
        screen.blit(play_again_text,(630,25))
        screen.blit(win_txt, (210,60))
        
        
    #Hands Display - Updates as cards are added
    px = 210
    dx = 210
    for i in p_hand:
        i.draw(screen,px,350)
        px += 30
    for i in d_hand:
        i.draw(screen,dx,100)
        dx += 30

    if player_points > 21:
        gamestate = 3

def dealer_turn():
    '''
    this function plays the entire dealer turn
    updates the display with correct values
    displays the win message
    '''
    global dealer_points
    global player_points
    global win_message

    d_hand[0].flip()
    dealer_points = point_calc(d_hand)
    while dealer_points < 17 and dealer_points < 22:
        d_hand.append(deck.draw())
        dealer_points = point_calc(d_hand)
    dpv_text = Arial40.render(str(dealer_points),1,BLACK)

    if len(p_hand) == 2 and player_points == 21:
        win_message = 'Player has Black Jack - Player Wins!'
    elif dealer_points > 21:
        win_message = 'Dealer Busted - Player Wins!'
    elif dealer_points >= player_points:
        win_message = 'Dealer Wins!'
    else:
        win_message = 'Player Wins!'

    

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
MS_Sans_Serif60 = pygame.font.SysFont("MS Sans Serif",60)


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
play = Rect(320, 250, 160, 60)
game_exit = Rect(320, 325, 160, 60)
quit_game = Rect(25, 10, 110, 50)

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
win_message = 'Player busted - Dealer wins!'

end = True
gamestate = 0
while end:
    if gamestate == 0:
        open_screen()
    if gamestate != 0:
        game()
   
    pygame.display.update()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()

        if event.type == MOUSEBUTTONUP and event.button == 1:
                if gamestate == 0:
                    if play.collidepoint(event.pos):
                        gamestate = 1
                    if game_exit.collidepoint(event.pos):
                        end = False
                        pygame.quit()
                if gamestate == 1:
                    if draw_button.collidepoint(event.pos):
                        p_hand.append(deck.draw())
                        player_points = point_calc(p_hand)
                    if stand_button.collidepoint(event.pos):
                        gamestate = 2
                        dealer_turn()
                    if quit_game.collidepoint(event.pos):
                        end = False
                        pygame.quit()
                if gamestate == 2 or gamestate == 3:    
                    if play_again.collidepoint(event.pos):
                        #Logic for resetting the game
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

                    if quit_game.collidepoint(event.pos):
                        end = False
                        pygame.quit()





