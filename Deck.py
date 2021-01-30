from Card import *
import random as r

class Deck():

    """
    creates a list of 52 unique card objects that would represent a
    standard deck of 52 playing cards - minus the jokers
    creates an empty list of discarded cards from the deck
    randomizes the cards
    """

    def __init__(self):
        self.deck_list = []
        self.discard_pile = []
        ranks = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX','SEVEN',
                 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
        points = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']

        for x in range (len(ranks)):
            for y in range (len(suits)):
                self.deck_list.append(Card(ranks[x],suits[y],points[x]))
        self.shuffle()

    def __str__(self):
        output = ''
        for x in range (len(self.deck_list)):
            output += str(self.deck_list[x])+ '\n'
        return output

    def __len__(self):
        return len(self.deck_list)

    def show_discards(self):
        if len(self.discard_pile) > 0:
            for c in self.discard_pile:
                print(c)
        else:
            print('Discard Pile Empty')

    def discard(self,c):
        self.discard_pile.append(c)

    def shuffle(self):
        end = len(self.deck_list) - 1
        while end > 0:
           swap_spot = r.randint(0,end)
           temp = self.deck_list[end]
           self.deck_list[end] = self.deck_list[swap_spot]
           self.deck_list[swap_spot] = temp
           end -= 1

    def draw(self):
        if len(self.deck_list) > 0:
            return self.deck_list.pop(0)
        else:
            if len(self.discard_pile) > 0:
                self.deck_list = self.discard_pile
                self.shuffle()
                return self.deck_list.pop(0)
            else:
                return 'There is no card avaiable to draw'
                

    
