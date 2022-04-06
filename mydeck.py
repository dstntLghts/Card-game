import random
import tkinter as tk
import tkinter.ttk as ttk

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
        

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.build()

    def build(self):
        play_btn = ttk.Button(self.root,text="Play",command=menu.play)
        quit_btn = ttk.Button(self.root,text="Quit",command=self.root.destroy)
        play_btn.pack()
        quit_btn.pack()
        self.root.mainloop()

    def play(self):
        print("Game Started")

    def select_players(self):
        pass

    def quit(self):
        print("Quiting game")

    def save_game(self):
        pass

    def load_game(self):
        pass

    def difficulty(self):
        pass


# test = Deck()
# test.show()
menu = Menu()
interface = GUI()
