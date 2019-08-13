import random

class Card(object):
    def __init__(self, suite, val):
        self.suite = suite
        self.value = val

    def show(self):
        value = self.value
        if value == 11:
            value = 'Jack'
        if value == 12:
            value = 'Queen'
        if value == 13:
            value = 'King'
        print(f'{value} of {self.suite}')

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suite in ['Spades', 'Clubs', 'Hearts', 'Diamonds']:
            for number in range(1,14):
                card = Card(suite, number)
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())

    def showHand(self):
        for card in self.hand:
            card.show()

    def  discard(self):
        return self.hand.pop()

deck = Deck()
deck.show()
deck.shuffle()
deck.show()