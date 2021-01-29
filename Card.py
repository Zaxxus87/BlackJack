import pygame
from pygame.locals import *
import os

class Card():

    def __init__(self, rank, suit, point_value):
        self.rank = rank
        self.suit = suit
        self.point_value = point_value
        self.up = True
        self.back_image = pygame.image.load(os.path.join('Images','card_back.jpg'))

        if  self.suit == 'HEARTS':
            if self.rank == 'ACE':
                self.front_image = pygame.image.load(os.path.join('Images','Ace_Hearts.jpg'))
            if self.rank == 'TWO':
                self.front_image = pygame.image.load(os.path.join('Images','Two_Hearts.jpg'))
            if self.rank == 'THREE':
                self.front_image = pygame.image.load(os.path.join('Images','Three_Hearts.jpg'))
            if self.rank == 'FOUR':
                self.front_image = pygame.image.load(os.path.join('Images','Four_Hearts.jpg'))
            if self.rank == 'FIVE':
                self.front_image = pygame.image.load(os.path.join('Images','Five_Hearts.jpg'))
            if self.rank == 'SIX':
                self.front_image = pygame.image.load(os.path.join('Images','Six_Hearts.jpg'))
            if self.rank == 'SEVEN':
                self.front_image = pygame.image.load(os.path.join('Images','Seven_Hearts.jpg'))
            if self.rank == 'EIGHT':
                self.front_image = pygame.image.load(os.path.join('Images','Eight_Hearts.jpg'))
            if self.rank == 'NINE':
                self.front_image = pygame.image.load(os.path.join('Images','Nine_Hearts.jpg'))
            if self.rank == 'TEN':
                self.front_image = pygame.image.load(os.path.join('Images','Ten_Hearts.jpg'))
            if self.rank == 'JACK':
                self.front_image = pygame.image.load(os.path.join('Images','Jack_Hearts.jpg'))
            if self.rank == 'QUEEN':
                self.front_image = pygame.image.load(os.path.join('Images','Queen_Hearts.jpg'))
            if self.rank == 'KING':
                self.front_image = pygame.image.load(os.path.join('Images','King_Hearts.jpg'))
        elif  self.suit == 'SPADES':
            if self.rank == 'ACE':
                self.front_image = pygame.image.load(os.path.join('Images','Ace_Spades.jpg'))
            if self.rank == 'TWO':
                self.front_image = pygame.image.load(os.path.join('Images','Two_Spades.jpg'))
            if self.rank == 'THREE':
                self.front_image = pygame.image.load(os.path.join('Images','Three_Spades.jpg'))
            if self.rank == 'FOUR':
                self.front_image = pygame.image.load(os.path.join('Images','Four_Spades.jpg'))
            if self.rank == 'FIVE':
                self.front_image = pygame.image.load(os.path.join('Images','Five_Spades.jpg'))
            if self.rank == 'SIX':
                self.front_image = pygame.image.load(os.path.join('Images','Six_Spades.jpg'))
            if self.rank == 'SEVEN':
                self.front_image = pygame.image.load(os.path.join('Images','Seven_Spades.jpg'))
            if self.rank == 'EIGHT':
                self.front_image = pygame.image.load(os.path.join('Images','Eight_Spades.jpg'))
            if self.rank == 'NINE':
                self.front_image = pygame.image.load(os.path.join('Images','Nine_Spades.jpg'))
            if self.rank == 'TEN':
                self.front_image = pygame.image.load(os.path.join('Images','Ten_Spades.jpg'))
            if self.rank == 'JACK':
                self.front_image = pygame.image.load(os.path.join('Images','Jack_Spades.jpg'))
            if self.rank == 'QUEEN':
                self.front_image = pygame.image.load(os.path.join('Images','Queen_Spades.jpg'))
            if self.rank == 'KING':
                self.front_image = pygame.image.load(os.path.join('Images','King_Spades.jpg'))
        elif  self.suit == 'DIAMONDS':
            if self.rank == 'ACE':
                self.front_image = pygame.image.load(os.path.join('Images','Ace_Diamonds.jpg'))
            if self.rank == 'TWO':
                self.front_image = pygame.image.load(os.path.join('Images','Two_Diamonds.jpg'))
            if self.rank == 'THREE':
                self.front_image = pygame.image.load(os.path.join('Images','Three_Diamonds.jpg'))
            if self.rank == 'FOUR':
                self.front_image = pygame.image.load(os.path.join('Images','Four_Diamonds.jpg'))
            if self.rank == 'FIVE':
                self.front_image = pygame.image.load(os.path.join('Images','Five_Diamonds.jpg'))
            if self.rank == 'SIX':
                self.front_image = pygame.image.load(os.path.join('Images','Six_Diamonds.jpg'))
            if self.rank == 'SEVEN':
                self.front_image = pygame.image.load(os.path.join('Images','Seven_Diamonds.jpg'))
            if self.rank == 'EIGHT':
                self.front_image = pygame.image.load(os.path.join('Images','Eight_Diamonds.jpg'))
            if self.rank == 'NINE':
                self.front_image = pygame.image.load(os.path.join('Images','Nine_Diamonds.jpg'))
            if self.rank == 'TEN':
                self.front_image = pygame.image.load(os.path.join('Images','Ten_Diamonds.jpg'))
            if self.rank == 'JACK':
                self.front_image = pygame.image.load(os.path.join('Images','Jack_Diamonds.jpg'))
            if self.rank == 'QUEEN':
                self.front_image = pygame.image.load(os.path.join('Images','Queen_Diamonds.jpg'))
            if self.rank == 'KING':
                self.front_image = pygame.image.load(os.path.join('Images','King_Diamonds.jpg'))
        elif  self.suit == 'CLUBS':
            if self.rank == 'ACE':
                self.front_image = pygame.image.load(os.path.join('Images','Ace_Clubs.jpg'))
            if self.rank == 'TWO':
                self.front_image = pygame.image.load(os.path.join('Images','Two_Clubs.jpg'))
            if self.rank == 'THREE':
                self.front_image = pygame.image.load(os.path.join('Images','Three_Clubs.jpg'))
            if self.rank == 'FOUR':
                self.front_image = pygame.image.load(os.path.join('Images','Four_Clubs.jpg'))
            if self.rank == 'FIVE':
                self.front_image = pygame.image.load(os.path.join('Images','Five_Clubs.jpg'))
            if self.rank == 'SIX':
                self.front_image = pygame.image.load(os.path.join('Images','Six_Clubs.jpg'))
            if self.rank == 'SEVEN':
                self.front_image = pygame.image.load(os.path.join('Images','Seven_Clubs.jpg'))
            if self.rank == 'EIGHT':
                self.front_image = pygame.image.load(os.path.join('Images','Eight_Clubs.jpg'))
            if self.rank == 'NINE':
                self.front_image = pygame.image.load(os.path.join('Images','Nine_Clubs.jpg'))
            if self.rank == 'TEN':
                self.front_image = pygame.image.load(os.path.join('Images','Ten_Clubs.jpg'))
            if self.rank == 'JACK':
                self.front_image = pygame.image.load(os.path.join('Images','Jack_Clubs.jpg'))
            if self.rank == 'QUEEN':
                self.front_image = pygame.image.load(os.path.join('Images','Queen_Clubs.jpg'))
            if self.rank == 'KING':
                self.front_image = pygame.image.load(os.path.join('Images','King_Clubs.jpg'))
                

    
    def __str__(self):
        return '{} of {} (Value = {})'.format(
            self.rank,self.suit,self.point_value)

    def draw(self,win,x,y):
        if self.up:
            win.blit(self.front_image,(x,y))
        else:
            win.blit(self.back_image, (x,y))

    def flip(self):
        if self.up:
            self.up = False
        else:
            self.up = True


    
    
