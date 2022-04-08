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
    def __init__(self,difficulty):
        self.difficulty=difficulty
        self.cards=[] 
        self.build(self.difficulty)
        self.shuffle()

    def build(self,diff_choice):

        if diff_choice=='easy':
            for s in ["♠","♣","♦","♥"]:
                for v in (10,'J','Q','K'):
                    self.cards.append(Card(s,v))
        elif diff_choice=='average':
            for s in ["♠","♣","♦","♥"]:
                for v in (1,2,3,4,5,6,7,8,9,10):
                    self.cards.append(Card(s,v))
        elif diff_choice=='hard':
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
        
class Menu:
     def __init__(self):
         pass

     def play():
         pass
    
class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.build()
        
    def build(self):
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#8cd921')
        play_btn = ttk.Button(self.root,text="Play",command=self.play,style='A.TButton')
        slc_players_btn = ttk.Button(self.root,text="Select Players",command=self.select_players,style='A.TButton')
        quit_btn = ttk.Button(self.root,text="Quit",command=self.root.destroy,style='A.TButton')
        play_btn.grid(row=0,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        slc_players_btn.grid(row=1,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        quit_btn.grid(row=2,column=0,ipadx=50,ipady=20,padx=30,pady=10)

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

test = Deck("hard")
test.show()
menu = Menu()
interface = GUI()
