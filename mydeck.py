from asyncio.windows_events import NULL
import random
import time
<<<<<<< HEAD
from itertools import cycle
=======

>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52
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
        if value in ["J","Q","K"]:
            self.score = 10
        elif value == "A":
            self.score = 1
<<<<<<< HEAD
=======
        else:
            self.score = int(self.value)

    def show(self):
        if self.open==False:
            print("id:",self.id," XX")
>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52
        else:
            self.score = int(self.value)

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
                for v in ("A","2","3","4","5","6","7","8","9","10"):
                    id=id+1
                    self.cards.append(Card(s,v,id))
            self.rows=4
            self.cols=10
        elif diff_choice=='hard':
            for s in ["♠","♣","♦","♥"]:
                for v in ("A","2","3","4","5","6","7","8","9","10",'J','Q','K'):
                    id=id+1
                    self.cards.append(Card(s,v,id))
            self.rows=4
            self.cols=13

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]


class Player:
    def __init__(self,name,score=0,myturn=0):
        self.name = name
        self.score = score
        self.myturn = myturn


class GUI:

    def __init__(self):
        self.ndeck = None
        self.root = None
        self.frame_a = None
        self.frame_b = None
        self.build_menu()

    def build_menu(self):
        self.root = tk.Tk()
        self.root.geometry("300x300+550+250") # Μεγεθος+θεση παραθυρου
        self.root.resizable(0,0) # Κανει το παραθυρο να μην επεκτεινεται
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#8cd921')  #
        # Κουμπια
        newgame_btn = ttk.Button(self.root,text="New game",command=self.difficulty,style='A.TButton')
        load_btn = ttk.Button(self.root,text="Load game",command=self.load_game,style='A.TButton')
        quit_btn = ttk.Button(self.root,text="Quit",command=self.root.destroy,style='A.TButton')
        # Τοποθετηση Κουμπιων
        newgame_btn.grid(row=0,column=0,ipadx=50,ipady=20,padx=45,pady=10)
        load_btn.grid(row=1,column=0,ipadx=50,ipady=20,padx=45,pady=10)
        quit_btn.grid(row=2,column=0,ipadx=50,ipady=20,padx=45,pady=10)
        # Εκκινηση παραθυρου
        self.root.mainloop()

    def difficulty(self): # after Player number next windows could be diff choice following the same manner.
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.geometry("300x300+550+250")
        self.root.resizable(0,0)
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#34a832',activebackground='#000000')
        style.configure('B.TButton', font=('Helvetica',12,),  background='#e8d502')
        style.configure('C.TButton', font=('Helvetica',12,),  background='#e81d02')
        easy = ttk.Button(self.root, text="Easy",command=lambda i="easy":self.create_deck(i),style='A.TButton')
        average = ttk.Button(self.root, text="Average", command=lambda i="average":self.create_deck(i),style='B.TButton')
        hard = ttk.Button(self.root, text="Hard", command=lambda i="hard":self.create_deck(i),style='C.TButton')
        easy.grid(row=0,column=0,ipadx=50,ipady=20,padx=50,pady=10)
        average.grid(row=1,column=0,ipadx=50,ipady=20,padx=50,pady=10)
        hard.grid(row=2,column=0,ipadx=50,ipady=20,padx=50,pady=10)
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
        self.frame_a = tk.Frame(self.root)
        card_id = 0
        for i in range(self.ndeck.rows):
            for j in range (self.ndeck.cols):
                card = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                                 command=lambda card_id=card_id,i=i,j=j:self.select_card(card_id,i,j))
                if self.ndeck.cards[card_id].open==True: #This section is added in order to load open cards, buggy visual
                    if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
                        card = tk.Label(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                height=3,width=5,font=("Helvetica"),fg="red")
                    else:
                        card = tk.Label(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                height=3,width=5,font=("Helvetica"))
                # late binding issue
                # using lamda to pass arguments
                card.grid(row=i,column=j)
                card_id += 1
        self.frame_a.grid(row=0,column=0)
        self.frame_b = tk.Frame(self.root)
        p = tk.Label(self.frame_b,text="Player",font=("Arial",12),relief="groove")
        s = tk.Label(self.frame_b,text="Score",font=("Helvetica",12),relief="groove")
        t = tk.Label(self.frame_b,text="Turn",font=("Helvetica",12),relief="groove")
        p.grid(row=0,column=0),s.grid(row=0,column=1),t.grid(row=0,column=2)
        for h in range (len(players)): #Players presentation
            player = tk.Label(self.frame_b,text=f"{players[h].name}",height=2,font=("Helvetica",12))
            player.grid(row=h+1,column=0)

            score = tk.Label(self.frame_b,text=f"{players[h].score}",height=2,font=("Helvetica",12))
            score.grid(row=h+1,column=1)

            turn = tk.Label(self.frame_b,text=f"{players[h].myturn}",height=2,font=("Helvetica",12))
            turn.grid(row=h+1,column=2)
        save_btn = ttk.Button(self.frame_b,text="Save Game",command=self.save_game)
<<<<<<< HEAD
        save_btn.grid(row=5,column=0,ipadx=5,ipady=5,padx=0,pady=20)
        quit_btn = ttk.Button(self.frame_b,text="Quit",command=self.root.destroy)
        quit_btn.grid(row=6,column=0,ipadx=5,ipady=5,padx=0,pady=20)
=======
        save_btn.grid(row=5,column=1,ipadx=5,ipady=5,padx=0,pady=20)
>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52
        self.frame_b.grid(row=0,column=1,padx=20)
        self.root.mainloop()


    def select_card(self,card_id,r,c):
        # κωδικας για επιλογη καρτας
        if self.ndeck.counter > 1:  # Removes fast pressing side effects
            return
        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
            card = tk.Label(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"),fg="red")
        else:
            card = tk.Label(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"))
        card.grid(row=r,column=c)
        self.ndeck.cards[card_id].open = True
        self.ndeck.cards_check.append(list((self.ndeck.cards[card_id],card_id,r,c)))
        self.ndeck.counter += 1 
        print(self.ndeck.counter)
        if self.ndeck.counter == 2:
            self.root.after(700,lambda : self.evaluate_cards())  # delay
<<<<<<< HEAD

=======
>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52

    def evaluate_cards(self):
        # Κωδικας για τσεκαρισμα αν ο παικτης εχει σκοραρει
        self.ndeck.counter = 0
        if self.ndeck.cards_check[0][0].value != self.ndeck.cards_check[1][0].value:
            card_1 = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                               command=lambda card_id=self.ndeck.cards_check[0][1],
                                              r=self.ndeck.cards_check[0][2],
                                              c=self.ndeck.cards_check[0][3]: self.select_card(card_id,r,c))
            card_2 = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                               command=lambda card_id=self.ndeck.cards_check[1][1],
                                              r=self.ndeck.cards_check[1][2],
                                              c=self.ndeck.cards_check[1][3]: self.select_card(card_id,r,c))
            card_1.grid(row=self.ndeck.cards_check[0][2],column=self.ndeck.cards_check[0][3])
            card_2.grid(row=self.ndeck.cards_check[1][2],column=self.ndeck.cards_check[1][3])
<<<<<<< HEAD
            self.ndeck.cards[self.ndeck.cards_check[0][1]].open=False #added this bc each card stayed at open=true state even when they should not
            self.ndeck.cards[self.ndeck.cards_check[1][1]].open=False
        self.a=self.ndeck.cards_check[0][0].score+self.ndeck.cards_check[1][0].score #Score from two cards for each round. future use
        self.player_turn(players,int(self.a)) #change turn and sum score function
=======
>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52
        self.ndeck.cards_check.clear()
        self.check_win() #Check if game is over



    def select_players(self):
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
        if num==1:
            players.append(Player("Player1"))
            players.append(Player("BOT"))
        else:
            for i in range(1,5):  # Adds Players
                if i == num:
                    for j in range(i):
                        players.append(Player(f"Player{j}"))
                    break
        players[0].myturn=1
        print(players)
        self.root.destroy()
        self.play()

    def player_turn(self,plist,s):
        pass #Not there yet =/
        # mylist = iter(plist)
        # x = next(mylist)    
        # x.myturn==1
        # x[-1].myturn==0
        # x[-1].score= x[-1].score+s #score sum 

        # #need new logic   
        # for h in range (len(plist)): #Players presentation refresh
        #     player = tk.Label(self.frame_b,text=f"{plist[h].name}",height=2,font=("Helvetica",12))
        #     player.grid(row=h+1,column=0)

        #     score = tk.Label(self.frame_b,text=f"{plist[h].score}",height=2,font=("Helvetica",12))
        #     score.grid(row=h+1,column=1)

        #     turn = tk.Label(self.frame_b,text=f"{plist[h].myturn}",height=2,font=("Helvetica",12))
        #     turn.grid(row=h+1,column=2)

    # Check if the game is over
    def check_win(self):
        print(len(self.ndeck.cards))
        s=0
        for i in range(0,len(self.ndeck.cards)):
           if self.ndeck.cards[i].open==True:
            s +=1
            
        print(s)
        if s==len(self.ndeck.cards):
            tk.messagebox.showinfo('information','GAME OVER')
            self.build_menu() #when score if fixed will add information

    def quit(self):
        print("Quiting game")

    def save_game(self):
<<<<<<< HEAD
        decksave = "decksave.pickle"
        players_save = "players_save.pickle"
        with open(decksave,'wb') as self.dbfile1:
            pickle.dump(self.ndeck,self.dbfile1)
        with open(players_save,'wb') as self.dbfile2:
            pickle.dump(players,self.dbfile2)
        print("Game saved")
        self.dbfile1.close()
        self.dbfile2.close()
=======
        filename = "gamesave.pickle" #test
        with open(filename,'r+b') as self.dbfile:
            pickle.dump(players,self.dbfile)
            pickle.dump(self.ndeck.cards_check,self.dbfile)
        print("Game saved")
        self.dbfile.close()
>>>>>>> 1c8e4bd20ac043feae6afe6b14382f55d0447f52

    def load_game(self):
        decksave = "decksave.pickle"
        players_save = "players_save.pickle"
        self.db1={}
        if os.path.getsize(decksave) > 0:
            with open(decksave,'rb') as self.dbfile1:
                self.db1 = pickle.load(self.dbfile1)
        else:
            tk.messagebox.showwarning('error', 'Erroneus/empty Dictionary')
            print("Erroneus/empty Dictionary")
            self.db1={}
        self.ndeck=self.db1
        self.db2={}
        if os.path.getsize(players_save) > 0:
            with open(players_save,'rb') as self.dbfile2:
                self.db2 = pickle.load(self.dbfile2)
        else:
            tk.messagebox.showwarning('error', 'Erroneus/empty Dictionary')
            print("Erroneus/empty Dictionary")
            self.db2={}
        players=self.db2
        self.root.destroy()
        self.play()

players = []
interface = GUI()

# Code DUMP (don't delete may use later)
