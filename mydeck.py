import random

class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
        self.open= False # Ανοιχτή/Κλειστή

    def show(self): 
        print("{}{}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards=[] 
        self.build()
        self.shuffle()

    def build(self):
        for s in ["♠","♣","♦","♥"]:
            for v in (1,2,3,4,5,6,7,8,9,10,'J','Q','K'):
                self.cards.append(Card(s,v))
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
        
    def show(self):
        for c in self.cards:
            c.show()

    def select_cards(card_choice):
        pass
        # Πατημα Κουμπιου
        # Επιλογη 1ης Καρτας
        # Επιλογη 2ης Καρτας
        # Έλεγχος αν ειναι ιδιες
        # Αν ΝΑΙ: Παραμενουν ανοιχτες και ποντος στον αντιστοιχο παικτη
        # Αν ΟΧΙ: Κλείνουνε και παιζει ο επομενος παικτης
  
class Player:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score

test = Deck()
test.show()