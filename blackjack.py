import random
import time

'''
A text based game of the Blackjack card game (21).
Developed by Noah Smiley and Riley Edmunds.
'''

class Deck():

    def __init__(self):
        self.deck = []
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.faces = [['Two',2],['Three',3],['Four',4],
                     ['Five',5],['Six',6],['Seven',7],['Eight',8],
                     ['Nine',9],['Ten',10],['Jack',10],['Queen',10],
                     ['King',10],['Ace',11]]

        #On instantiaion of the class, a deck of 52 cards is created.
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
        self.newDeck = Deck()
        self.newDeck.shuffle()
        self.deck= self.newDeck.deck
        self.userTotal = 0
        self.dealerTotal = 0
        print("Welcome to Noah and Riley's Blackjack game!\n")

    def new_round(self):
        #Card hands for the dealer and user
        userCard = [self.newDeck.select_card(), self.newDeck.select_card()]
        dealerCard = [self.newDeck.select_card(), self.newDeck.select_card()]
        self.userTotal = userCard[0][1][1]+userCard[1][1][1]

        print((f"You were dealt:\nThe {userCard[0][1][0]} of {userCard[0][0]}"))
        print((f"And The {userCard[1][1][0]} of {userCard[1][0]}"))
        print((f"Your current total is: {self.userTotal}"))

        self.hit(userCard)

    def hit(self,userCard):
        while self.userTotal<=20:
            result = input("Would you like to hit? y/n")
            if result == 'y' or result == 'Y':
                userCard.append(self.newDeck.select_card())
            else:
                break

        return userCard

def main():
    newGame = GameLogic()
    newGame.new_round()
main()
