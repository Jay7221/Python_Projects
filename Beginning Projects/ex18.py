#! python3
# ex18.py

import random

class Card():
    '''Represent a standard playing card.'''

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s'%(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    '''Represent a deck of playing cards.'''
    def __init__(self):
        self.cards = list()
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = list()
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, no_hands, cards_per_hand):
        hands = list()
        for i in range(no_hands):
            hand = Hand()
            self.move_cards(hand, cards_per_hand)
            hands.append(hand)
        return hands
            

class Hand(Deck):
    '''Represents a hand of playing cards.'''
    def __init__(self, label = ''):
        self.cards = []
        self.label = label
        
