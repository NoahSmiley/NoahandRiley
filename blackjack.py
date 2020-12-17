import random

'''
A text based game of the Blackjack card game (21).
Developed by Noah Smiley and Riley Edmunds.
'''

class Deck():

    def __init__(self):
        self.deck = []
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.faces = [['Ace',1],['Two',2],['Three',3],['Four',4],
                     ['Five',5],['Six',6],['Seven',7],['Eight',8],
                     ['Nine',9],['Ten',10],['Jack',11],['Queen',12],
                     ['King',13]]

        #On instantiaion of the class, a deck of 64 cards is created.
        for suit in self.suits:
            for face in self.faces:
                x = (suit,face)
                self.deck.append(x)

    #Shuffle method to shuffle the deck.
    def shuffle(self):
        random.shuffle(self.deck)

    def select_card(self):
        return self.deck.pop()

    #Dunder str method to print the Deck out.
    def __str__(self):
        strings=[]
        for i in range(len(self.deck)):
            strings.append(f" The {self.deck[i][1][0]} of {self.deck[i][0]}")
        return '\n'.join(strings)

class GameLogic(Deck):

    def __init__(self):
        deck = Deck()
        deck.shuffle()

        selectedCard = deck.select_card()

        print(selectedCard)


def main():

    newGame = GameLogic()

main()
