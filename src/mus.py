#!/usr/bin/env python3
import operator
import random

class Card:
    def __init__(self, val, col):
        assert( val in range(1,8) + range(10,13) )
        self.val = val
        assert( col in range(1, 5) )
        self.col = col

    def getGame(self):
        if self.val < 10:
            return self.val
        else:
            return 10

    def __repr__(self):
        # res = "Card info: val " +str(self.val) + " - col " + str(self.col) + " "
        res = "#" +str(self.val) + "(" + str(self.col) + ") "
        return res

class Deck:
    def __init__(self):
        self.cards = list()
        for val in range(1,8)+range(10,13):
            for col in range(1,5):
                self.cards.append(Card(val, col))
                
    def __repr__(self):
        res = "Deck info:\n"
        for card in self.cards:
            res += str(card)
        return res
    
    def pop(self, card_numb):
        res = []
        for i in range (card_numb):
            res.append (self.cards.pop(random.randrange(len(self.cards))))
        return res

    def getCardNumb(self):
        return len(self.cards)

class Hand:
    def __init__(self, l):
        assert(len(l) == 4)
        self.cards = l
        self.cards.sort(key= operator.attrgetter('val'))
        
    def __repr__(self):
        res = "Hand info:\n\t"
        for card in self.cards:
            res += str(card)
        res += "\n\tpairs: " + str(self.hasPairs()) + " (" + str(self.hasPairsXXYZ()) + " " + str(self.hasPairsXXXY()) + " " + str(self.hasPairsXXYY()) + " " + ")"
        res += "\n\tgame: " + str(self.hasGame()) + " " + str(self.getGame())
        return res
        
    def getGame(self):
        res = 0
        for card in self.cards:
            res += card.getGame()
        return res
    
    def hasGame(self):
        return self.getGame() > 30
    
    def hasPairs(self):
        cards_val = [self.cards[0].val, self.cards[1].val, self.cards[2].val, self.cards[3].val]
        return len(set(cards_val)) < 4

    def hasPairsXXYZ(self):
        cards_val = [self.cards[0].val, self.cards[1].val, self.cards[2].val, self.cards[3].val]
        return len(set(cards_val)) == 3

    def hasPairsXXXY(self):
        return (self.cards[0].val == self.cards[1].val == self.cards[2].val or self.cards[1].val == self.cards[2].val == self.cards[3].val) and not self.hasPairsXXYY()

    def hasPairsXXYY(self):
        return self.cards[0].val == self.cards[1].val and self.cards[2].val == self.cards[3].val

def printStats(name, numb, tot_numb):
    print (name , '{:.1%}'.format(float(numb)/tot_numb), tot_numb)

if __name__ == "__main__":
    print ("begin")

    N = 10000
    n_hasPairs = 0
    n_hasPairsXXYZ = 0
    n_hasPairsXXXY = 0
    n_hasPairsXXYY = 0
    n_hasGame = 0
    n_has31_if_hasGame = 0
    for i in range(N):
        d = Deck()
        h = Hand(d.pop(4))
        # print (h)

        if h.hasPairs():
            n_hasPairs += 1
        if h.hasPairsXXYZ():
            n_hasPairsXXYZ += 1
        if h.hasPairsXXXY():
            n_hasPairsXXXY += 1
        if h.hasPairsXXYY():
            n_hasPairsXXYY += 1
        
        if h.hasGame():
            n_hasGame += 1
            if h.getGame() == 31:
                n_has31_if_hasGame += 1
    
    printStats("hasPairs", n_hasPairs, N)
    printStats("hasPairsXXYZ", n_hasPairsXXYZ, N)
    printStats("hasPairsXXXY", n_hasPairsXXXY, N)
    printStats("hasPairsXXYY", n_hasPairsXXYY, N)
    
    printStats("hasGame", n_hasGame, N)
    printStats("has31_if_hasGame", n_has31_if_hasGame, n_hasGame)
    
    # h = Hand([Card(10,1), Card(5,3), Card(10,4), Card(5,1)])
    # print (h)
    print ("happy end")