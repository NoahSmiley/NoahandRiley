class Cards():

    def __init__(self):

        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        faces =[['Ace',1],['Two',2],['Three',3],['Four',4],
               ['Five',5],['Six',6],['Seven',7],['Eight',8],
               ['Nine',9],['Ten',10],['Jack',11],['Queen',12],
               ['King',13]]
        deck=[]
        #Making
        for suit in suits:
            for face in faces:
                x = (suit,face)
                deck.append(x)

        for i in range(len(deck)):
            print(f" The {deck[i][1][0]} of {deck[i][0]}")

newCardDeck = Cards()
