import random
from unicodedata import name
#import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
import pickle
import os


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
        self.cards_check = []
        self.counter = 0
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


class Player:
    def __init__(self,name,score=0,myturn=0):
        self.name = name
        self.score = score
        self.myturn=myturn


class GUI:

    def __init__(self):
        self.ndeck = None
        self.build_menu()

    def build_menu(self):
        self.root = tk.Tk()
        self.root.geometry("300x400+550+250") # Μεγεθος+θεση παραθυρου
        self.root.resizable(0,0) # Κανει το παραθυρο να μην επεκτεινεται
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#8cd921')  #
        # Κουμπια
        load_btn = ttk.Button(self.root,text="Load game",command=self.load_game,style='A.TButton')
        difficulty_btn = ttk.Button(self.root,text="New game",command=self.difficulty,style='A.TButton')
        quit_btn = ttk.Button(self.root,text="Quit",command=self.root.destroy,style='A.TButton')
        # Τοποθετηση Κουμπιων
        load_btn.grid(row=0,column=0,ipadx=50,ipady=20,padx=50,pady=10)
        difficulty_btn.grid(row=1,column=0,ipadx=50,ipady=20,padx=50,pady=10)
        quit_btn.grid(row=2,column=0,ipadx=50,ipady=20,padx=50,pady=10)
        # Εκκινηση παραθυρου
        self.root.mainloop()

    def difficulty(self): # after Player number next windows could be diff choice following the same manner.
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.geometry("300x400+550+250")
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
        self.select_players()

    def play(self):
        print("Game Started")
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.title("Cards Game")
        self.root.resizable(0,0)
        self.root.geometry("+550+250")
        save_btn = ttk.Button(self.root,text="Save Game",command=self.save_game,style='A.TButton')
        card_id = 0
        for i in range(self.ndeck.rows):
            for j in range (self.ndeck.cols):
                card = tk.Button(self.root,text="🂠",height=3,width=5,font=("Helvetica"),
                                 command=lambda card_id=card_id,i=i,j=j:self.select_card(card_id,i,j))
                # late binding issue
                # using lamda to pass arguments
                
                card.grid(row=i,column=j)
                card_id += 1
        for h in range (len(players)): #Players presentation 
                player = tk.Label(self.root,text=f"{players[h].name}",height=3,width=5)
                player.grid(row=(self.ndeck.rows+h),column=0)
 
                score = tk.Label(self.root,text=f"{players[h].score}",height=3,width=5)
                score.grid(row=(self.ndeck.rows+h),column=1)

                turn = tk.Label(self.root,text=f"{players[h].myturn}",height=3,width=5)
                turn.grid(row=(self.ndeck.rows+h),column=2)
        save_btn = ttk.Button(self.root,text="Save",command=self.save_game)
        save_btn.grid(row=(self.ndeck.rows+(len(players)+1)),column=0,ipadx=0,ipady=0,padx=5,pady=5)
        self.root.mainloop()


    def select_card(self,card_id,r,c):
        # κωδικας για επιλογη καρτας
        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
            card = tk.Label(self.root,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"),fg="red")
        else:
            card = tk.Label(self.root,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"))
        card.grid(row=r,column=c)
        self.ndeck.cards[card_id].open = True
        self.ndeck.cards_check.append(list((self.ndeck.cards[card_id],card_id,r,c)))
        print(self.ndeck.cards_check)
        self.ndeck.counter += 1
        if self.ndeck.counter == 2:
            self.evaluate_cards()


    def evaluate_cards(self):
        # Κωδικας για τσεκαρισμα αν ο παικτης εχει σκοραρει
        # ΠΡΕΠΕΙ ΝΑ ΒΑΛΟΥΜΕ DELAY με το tk.after()
        print("ENTERED CHEK")
        if self.ndeck.cards_check[0][0].value != self.ndeck.cards_check[1][0].value:
            print("MUST HIDE")
            card_1 = tk.Button(self.root,text="🂠",height=3,width=5,font=("Helvetica"),
                             command=lambda card_id=self.ndeck.cards_check[0][1],
                                            r=self.ndeck.cards_check[0][2],
                                            c=self.ndeck.cards_check[0][3]: self.select_card(card_id,r,c))
            card_2 = tk.Button(self.root,text="🂠",height=3,width=5,font=("Helvetica"),
                             command=lambda card_id=self.ndeck.cards_check[1][1],
                                            r=self.ndeck.cards_check[1][2],
                                            c=self.ndeck.cards_check[1][3]: self.select_card(card_id,r,c))
            card_1.grid(row=self.ndeck.cards_check[0][2],column=self.ndeck.cards_check[0][3])
            card_2.grid(row=self.ndeck.cards_check[1][2],column=self.ndeck.cards_check[1][3])
        self.ndeck.counter = 0
        self.ndeck.cards_check.clear()


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
        self.play()

    def quit(self):
        print("Quiting game")

    def save_game(self):
        filename = "gamesave.pickle" #test
        with open(filename,'r+b') as self.dbfile:
            pickle.dump(players,self.dbfile)
            pickle.dump(self.ndeck.cards_check,self.dbfile)
        print("Game saved")        
        self.dbfile.close()

    def load_game(self):
        filename = "gamesave.pickle" #test
        self.db={}
        if os.path.getsize(filename) > 0:
            with open(filename,'rb') as self.dbfile:
                self.db = pickle.load(self.dbfile)
        else:
            tk.messagebox.showwarning('error', 'Erroneus/empty Dictionary')
            print("Erroneus/empty Dictionary")
            self.db={}
        return self.db

players = []
interface = GUI()

# Code DUMP (don't delete may use later)