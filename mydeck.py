import random
from unicodedata import name
#import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

class Card:
    def __init__(self,suit,value,id):
        self.suit=suit
        self.value=value
        self.id=id
        self.open= False # Ανοιχτή/Κλειστή

    def show(self):
        if self.open==False:
            print("id:",self.id," XX")
        else:
            print("id:",self.id,"{}{}".format(self.value,self.suit))

class Deck:
    def __init__(self,difficulty):
        self.cards=[]
        self.rows=0
        self.cols=0
        self.build(difficulty)
        self.shuffle()

    def build(self,diff_choice):
        id=0
        if diff_choice=='easy':    
            for s in ["♠","♣","♦","♥"]:
                for v in ("10",'J','Q','K'):
                    id=id+1
                    self.cards.append(Card(s,v,id))
            self.rows=4
            self.cols=4
        elif diff_choice=='average':
            for s in ["♠","♣","♦","♥"]:
                for v in ("1","2","3","4","5","6","7","8","9","10"):
                    id=id+1
                    self.cards.append(Card(s,v,id))
            self.rows=4
            self.cols=10
        elif diff_choice=='hard':
            for s in ["♠","♣","♦","♥"]:
                for v in ("1","2","3","4","5","6","7","8","9","10",'J','Q','K'):
                    id=id+1
                    self.cards.append(Card(s,v,id))
            self.rows=4
            self.cols=13

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def show_deck(self):
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
        self.ndeck = None
        self.build_menu()

    def build_menu(self):
        self.root = tk.Tk()
        self.root.geometry("400x300+550+250") # Μεγεθος+θεση παραθυρου
        self.root.resizable(0,0) # Κανει το παραθυρο να μην επεκτεινεται
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#8cd921')  #
        # Κουμπια
        play_btn = ttk.Button(self.root,text="Play",command=self.difficulty,style='A.TButton')
        slc_players_btn = ttk.Button(self.root,text="Select Players",command=self.select_players,style='A.TButton')
        quit_btn = ttk.Button(self.root,text="Quit",command=self.root.destroy,style='A.TButton')
        # Τοποθετηση Κουμπιων
        play_btn.grid(row=0,column=0,ipadx=50,ipady=20,padx=90,pady=10)
        slc_players_btn.grid(row=1,column=0,ipadx=50,ipady=20,padx=90,pady=10)
        quit_btn.grid(row=2,column=0,ipadx=50,ipady=20,padx=90,pady=10)
        # Εκκινηση παραθυρου
        self.root.mainloop()

    def play(self):
        print("Game Started")
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.title("Cards Game")
        self.root.resizable(0,0)
        self.root.geometry("+550+250")
        card_id = 0
        for i in range(self.ndeck.rows):
            for j in range (self.ndeck.cols):
                card = tk.Button(self.root,text="🂠",height=3,width=5,font=("Helvetica"),
                                 command=lambda card_id=card_id,i=i,j=j:self.select_card(card_id,i,j))
                # late binding issue
                # using lamda to pass arguments
                card.grid(row=i,column=j)
                card_id += 1
        self.root.mainloop()


    def select_card(self,card_id,r,c):
        # κωδικας για επιλογη καρτας
        if self.ndeck.cards[card_id].suit in ["♦","♥"]:
            card = tk.Label(self.root,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"),fg="red")
        else:
            card = tk.Label(self.root,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"))
        card.grid(row=r,column=c)
        self.ndeck.cards[card_id].open = True

    def evaluate_cards(self):
        # Κωδικας για check αν ο παικτης εχει σκοραρει
        pass



    def select_players(self):
        #  Under construction
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.geometry("300x400+550+250")  # Μεγεθος+θεση παραθυρου
        self.root.resizable(0,0)
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style()  # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#111111')
        player1 = ttk.Button(self.root, text="1 Player", command=lambda i=1:self.action_select_players(i))
        player2 = ttk.Button(self.root, text="2 Players", command=lambda i=2:self.action_select_players(i))
        player3 = ttk.Button(self.root, text="3 Players", command=lambda i=3:self.action_select_players(i))
        player4 = ttk.Button(self.root, text="4 Players", command=lambda i=4:self.action_select_players(i))
        player1.grid(row=0,column=0,ipadx=50,ipady=20,padx=63,pady=10)
        player2.grid(row=1,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        player3.grid(row=2,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        player4.grid(row=3,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        self.root.mainloop()

    def action_select_players(self,num):
        players.clear()  # Remove previous players
        for i in range(1,5):  # Adds Players
            if i == num:
                for j in range(i):
                    players.append(Player(f"Player{j}"))
                break
        print(players)
        self.root.destroy()
        self.build_menu()

    def quit(self):
        print("Quiting game")

    def save_game(self):
        pass

    def load_game(self):
        pass

    def difficulty(self): # after Player number next windows could be diff choice following the same manner.
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.geometry("300x300+550+250")
        self.root.resizable(0,0)
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#111111')
        easy = ttk.Button(self.root, text="Easy",command=lambda i="easy":self.create_deck(i))
        average = ttk.Button(self.root, text="Average", command=lambda i="average":self.create_deck(i))
        hard = ttk.Button(self.root, text="Hard", command=lambda i="hard":self.create_deck(i))
        easy.grid(row=0,column=0,ipadx=50,ipady=20,padx=63,pady=10)
        average.grid(row=1,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        hard.grid(row=2,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        self.root.mainloop()

    def create_deck(self,mode): #creates a shuffled deck depending users choice 
        self.ndeck=Deck(mode)
        self.play()
        self.ndeck.show_deck()


players = []
interface = GUI()


# Code DUMP (don't delete may use later)
