import random
class Cards():

    def __init__(self):
        self.deck=[]
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.faces =[['Ace',1],['Two',2],['Three',3],['Four',4],
                    ['Five',5],['Six',6],['Seven',7],['Eight',8],
                    ['Nine',9],['Ten',10],['Jack',11],['Queen',12],
                    ['King',13]]

        for suit in self.suits:
            for face in self.faces:
                x = (suit,face)
                self.deck.append(x)

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        strings=[]
        for i in range(len(self.deck)):
            strings.append(f" The {self.deck[i][1][0]} of {self.deck[i][0]}")
        return '\n'.join(strings)

def main():
    newCardDeck = Cards()
    newCardDeck.shuffle()
    print(newCardDeck)
main()
