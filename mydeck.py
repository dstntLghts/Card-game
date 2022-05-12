from asyncio.windows_events import NULL
import random
import time
from itertools import cycle
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
        self.row=0
        self.col=0
        self.open= False # Ανοιχτή/Κλειστή
        if value in ["J","Q","K"]:
            self.score = 10
        elif value == "A":
            self.score = 1
        else:
            self.score = int(self.value)

class Deck:
    def __init__(self,difficulty):
        self.cards=[]   # List of Cards
        self.closed_cards=[]  # List of closed cards
        self.cards_check = []   # List of cards to be checked
        self.counter = 0   # Counter for opened cards in each turn
        self.rows=0
        self.cols=0
        self.build(difficulty)
        self.shuffle()
        # self.coordinate_cards()



    def build(self,diff_choice):
        id=0
        if diff_choice=='easy':
            for s in ["♠","♣","♦","♥"]:
                for v in ("10",'J','Q','K'):
                    self.cards.append(Card(s,v,id))
                    self.closed_cards.append(Card(s,v,id))
                    id=id+1
            self.rows=4
            self.cols=4
        elif diff_choice=='average':
            for s in ["♠","♣","♦","♥"]:
                for v in ("A","2","3","4","5","6","7","8","9","10"):
                    self.cards.append(Card(s,v,id))
                    self.closed_cards.append(Card(s,v,id))
                    id=id+1
            self.rows=4
            self.cols=10
        elif diff_choice=='hard':
            for s in ["♠","♣","♦","♥"]:
                for v in ("A","2","3","4","5","6","7","8","9","10",'J','Q','K'):
                    self.cards.append(Card(s,v,id))
                    self.closed_cards.append(Card(s,v,id))
                    id=id+1
            self.rows=4
            self.cols=13

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]

    def coordinate_cards(self):
        c=0 # counter
        for i in range(self.rows):
            for j in range(self.cols):
                self.cards[c].row = i
                self.cards[c].col = j
                c+=1



class Player:
    def __init__(self,name,score=0,myturn=False):
        self.name = name
        self.score = score
        self.myturn = myturn

class Bot:
    def __init__(self,score=0,myturn=False):
        self.name = "BOT"
        self.score = score
        self.myturn = myturn
        self.memory = []

class GUI:

    def __init__(self):
        self.ndeck = None
        self.root = None
        self.frame_a = None
        self.frame_b = None
        self.bot = Bot()
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

    def difficulty(self):
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
        easy = ttk.Button(self.root, text="Easy",command=lambda mode="easy":self.create_deck(mode),style='A.TButton')
        average = ttk.Button(self.root, text="Average", command=lambda mode="average":self.create_deck(mode),style='B.TButton')
        hard = ttk.Button(self.root, text="Hard", command=lambda mode="hard":self.create_deck(mode),style='C.TButton')
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
        self.root.geometry("+400+250")
        self.frame_a = tk.Frame(self.root)
        n = 0
        if type(players[1]) is Bot:
            for i in range(self.ndeck.rows):
                for j in range (self.ndeck.cols):
                    card_id = self.ndeck.cards[n].id
                    self.ndeck.cards[n].row = i
                    self.ndeck.cards[n].col = j
                    card = tk.Button(self.frame_a, text="🂠", height=3, width=5, font=("Helvetica"),
                                     command=lambda card_id=card_id,row=i,col=j:self.bot_select_card(card_id, row, col))
                    if self.ndeck.cards[card_id].open==True: #This section is added in order to load open cards, buggy visual
                        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
                            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                    height=3,width=5,font=("Helvetica"),state="disabled",disabledforeground="red")
                        else:
                            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                    height=3,width=5,font=("Helvetica"),state="disabled",disabledforeground="black")
                    # late binding issue
                    # using lamda to pass arguments
                    card.grid(row=i,column=j)
                    n += 1
            for i in self.ndeck.cards:
                print(f"id {i.id}, row {i.row+1}, col {i.col+1}   S= {i.value}{i.suit}")
            print(20*"-")
        else:
            for i in range(self.ndeck.rows):
                for j in range (self.ndeck.cols):
                    card_id = self.ndeck.cards[n].id
                    self.ndeck.cards[n].row = i
                    self.ndeck.cards[n].col = j
                    card = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                                     command=lambda card_id=card_id,row=i,col=j:self.select_card(card_id,row,col))
                    if self.ndeck.cards[card_id].open==True: #This section is added in order to load open cards, buggy visual
                        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
                            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                             height=3,width=5,font=("Helvetica"),state="disabled",disabledforeground="red")
                        else:
                            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                                             height=3,width=5,font=("Helvetica"),state="disabled",disabledforeground="black")
                    # late binding issue
                    # using lamda to pass arguments
                    card.grid(row=i,column=j)
                    n += 1
        self.frame_a.grid(row=0,column=0)
        self.frame_b = tk.Frame(self.root)
        p = tk.Label(self.frame_b,text="Player",font=("Arial",12),background="#d1d1d1",)
        s = tk.Label(self.frame_b,text="Score",font=("Helvetica",12),background="#d1d1d1")
        t = tk.Label(self.frame_b,text="Turn",font=("Helvetica",12),background="#d1d1d1")
        p.grid(row=0,column=0,padx=5,ipadx=2,ipady=2)
        s.grid(row=0,column=1,padx=5,ipadx=2,ipady=2)
        t.grid(row=0,column=2,padx=5,ipadx=2,ipady=2)
        for h in range (len(players)): #Players presentation
            player = tk.Label(self.frame_b,text=f"{players[h].name}",height=2,font=("Helvetica",12))
            player.grid(row=h+1,column=0)

            score = tk.Label(self.frame_b,text=f"{players[h].score}",height=2,font=("Helvetica",12))
            score.grid(row=h+1,column=1)

            turn = tk.Label(self.frame_b,text=f"{'◄' if players[h].myturn else ' '}",height=2,font=("Helvetica",12))
            turn.grid(row=h+1,column=2)
        save_btn = ttk.Button(self.frame_b,text="Save Game",command=self.save_game)
        save_btn.grid(row=5,column=0,ipadx=5,ipady=5,padx=0,pady=20)
        quit_btn = ttk.Button(self.frame_b,text="Quit",command=self.root.destroy)
        quit_btn.grid(row=6,column=0,ipadx=5,ipady=5,padx=0,pady=20)
        self.frame_b.grid(row=0,column=1,padx=20)
        self.root.mainloop()


    def select_card(self,card_id,r,c):
        # κωδικας για επιλογη καρτας
        if self.ndeck.counter > 1:  # Prevents 3rd card to be pressed
            return
        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"),disabledforeground="red",state="disabled")
        else:
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                            height=3,width=5,font=("Helvetica"),disabledforeground="black",state="disabled")
        card.grid(row=r,column=c)
        self.ndeck.cards[card_id].open = True
        self.ndeck.cards_check.append(list((self.ndeck.cards[card_id],card_id,r,c)))
        self.ndeck.counter += 1
        if self.ndeck.counter == 2:
            self.root.after(700,lambda : self.evaluate_cards())  # delay


    def bot_select_card(self, card_id, r, c):
        # κωδικας για επιλογη καρτας
        if self.ndeck.counter > 1:  # Prevents 3rd card to be pressed
            return 0
        if self.bot.myturn:
            return 0
        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"),disabledforeground="red",state="disabled")
        else:
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"),disabledforeground="black",state="disabled")
        card.grid(row=r,column=c)
        self.ndeck.cards[card_id].open = True
        print(f"player id {self.ndeck.cards[card_id].id}  row {self.ndeck.cards[card_id].row+1}   col {self.ndeck.cards[card_id].col+1}"
              f" S= {self.ndeck.cards[card_id].suit}{self.ndeck.cards[card_id].value}")
        self.ndeck.cards_check.append(list((self.ndeck.cards[card_id],card_id,r,c)))
        self.ndeck.counter += 1
        if self.ndeck.counter == 2:
            self.root.after(700, lambda : self.bot_evaluate_cards())  # delay


    def bot_evaluate_cards(self):
        # Κωδικας για τσεκαρισμα αν ο παικτης εχει σκοραρει
        self.ndeck.counter = 0
        card1_obj = self.ndeck.cards_check[0][0]
        card2_obj = self.ndeck.cards_check[1][0]
        card1_id = self.ndeck.cards_check[0][1]
        card2_id = self.ndeck.cards_check[1][1]
        card1_row = self.ndeck.cards_check[0][2]
        card2_row = self.ndeck.cards_check[1][2]
        card1_col = self.ndeck.cards_check[0][3]
        card2_col = self.ndeck.cards_check[1][3]
        self.score_stack= card1_obj.score + card2_obj.score #Score from two cards for each round.
        if card1_obj.value != card2_obj.value:
            card_1 = tk.Button(self.frame_a, text="🂠", height=3, width=5, font=("Helvetica"),
                               command=lambda card_id=card1_id,
                                              r=card1_row,
                                              c=card1_col: self.bot_select_card(card_id, r, c))
            card_2 = tk.Button(self.frame_a, text="🂠", height=3, width=5, font=("Helvetica"),
                               command=lambda card_id=card2_id,
                                              r=card2_row,
                                              c=card2_col: self.bot_select_card(card_id, r, c))
            card_1.grid(row=card1_row,column=card1_col)
            card_2.grid(row=card2_row,column=card2_col)
            self.ndeck.cards[card1_id].open=False # close cards
            self.ndeck.cards[card2_id].open=False
            self.score_stack=0  # no scoring
        self.bot_player_turn(players, int(self.score_stack), self.ndeck.cards_check) #change turn and sum score function
        self.ndeck.cards_check.clear()   # removes cards
        self.check_win(players) #Check if game is over
        if players[1].myturn:
            self.root.after(50,self.bot_choose_card())
            self.root.after(50,self.bot_choose_card())

    def bot_choose_card(self):
        # Its still buggy but at least it does play
        # Opens the same card sometimes
        self.ndeck.counter += 1
        # print(rand_num)
        while True:
            rand_num = random.randint(0,len(self.ndeck.cards)-1)
            if self.ndeck.cards[rand_num].open == False:
                break
        self.ndeck.cards[rand_num].open = True
        card_id = self.ndeck.cards[rand_num].id

        if self.ndeck.cards[card_id].suit in ["♦","♥"]: # Adds red color
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"),disabledforeground="red",state="disabled")
        else:
            card = tk.Button(self.frame_a,text=f"{self.ndeck.cards[card_id].value}{self.ndeck.cards[card_id].suit}",
                             height=3,width=5,font=("Helvetica"),disabledforeground="black",state="disabled")
        r=self.ndeck.cards[card_id].row
        c=self.ndeck.cards[card_id].col
        card.grid(row=r,column=c)
        self.ndeck.cards_check.append(list((self.ndeck.cards[card_id],self.ndeck.cards[card_id].id,r,c)))
        print(f"bot id {self.ndeck.cards[card_id].id}   row {self.ndeck.cards[card_id].row+1}  col {self.ndeck.cards[card_id].col+1}"
              f" S= {self.ndeck.cards[card_id].suit}{self.ndeck.cards[card_id].value}")
        if self.ndeck.counter < 2:
            self.root.after(1500, lambda : self.bot_evaluate_cards())


    def evaluate_cards(self):
        # Κωδικας για τσεκαρισμα αν ο παικτης εχει σκοραρει
        self.ndeck.counter = 0
        card1_obj = self.ndeck.cards_check[0][0]
        card2_obj = self.ndeck.cards_check[1][0]
        card1_id = self.ndeck.cards_check[0][1]
        card2_id = self.ndeck.cards_check[1][1]
        card1_row = self.ndeck.cards_check[0][2]
        card2_row = self.ndeck.cards_check[1][2]
        card1_col = self.ndeck.cards_check[0][3]
        card2_col = self.ndeck.cards_check[1][3]
        self.score_stack= card1_obj.score + card2_obj.score #Score from two cards for each round.
        if card1_obj.value != card2_obj.value:
            card_1 = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                               command=lambda card_id=card1_id,
                                              r=card1_row,
                                              c=card1_col: self.select_card(card_id,r,c))
            card_2 = tk.Button(self.frame_a,text="🂠",height=3,width=5,font=("Helvetica"),
                               command=lambda card_id=card2_id,
                                              r=card2_row,
                                              c=card2_col: self.select_card(card_id,r,c))
            card_1.grid(row=card1_row,column=card1_col)
            card_2.grid(row=card2_row,column=card2_col)
            self.ndeck.cards[card1_id].open=False #added this bc each card stayed at open=true state even when they should not
            self.ndeck.cards[card2_id].open=False
            self.score_stack=0
        self.player_turn(players, int(self.score_stack), self.ndeck.cards_check) #change turn and sum score function
        self.ndeck.cards_check.clear()
        self.check_win(players) #Check if game is over



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
            players.append(Player("Player_1"))
            players.append(self.bot)
        else:
            for i in range(2,5):  # Adds Players
                if i == num:
                    for j in range(i):
                        players.append(Player(f"Player_{j+1}"))
                    break
        players[0].myturn=True
        self.root.destroy()
        self.play()


    def bot_player_turn(self,plist,s,dlist): # player turn toggle function
        # p,d list player, deck list

        for i in range(len(plist)):
            if plist[i].myturn==True:   # if player turn
                plist[i].score += s  # adds score
                if  dlist[0][0].value=='J' and dlist[1][0].value=='J': # Wildcard "JJ"
                    # player doesnt lose turn
                    break
                plist[i].myturn= False  # loses turn
                if dlist[0][0].value=='K' and dlist[1][0].value=='K': # Wildcard "KK"
                    if i == (len(plist)-1):  # if last player
                        plist[1].myturn = True  # second player plays
                        break
                    if i == (len(plist)-2):  # if second last player
                        plist[0].myturn = True  # first player plays
                        break
                    else:
                        plist[i+2].myturn = True
                        break
                if i == (len(plist)-1):  # if last player
                    plist[0].myturn = True  # first player plays
                else:
                    plist[i+1].myturn = True
                break



        for h in range (len(plist)): #Players presentation refresh
            player = tk.Label(self.frame_b,text=f"{plist[h].name}",height=2,font=("Helvetica",12))
            player.grid(row=h+1,column=0)

            score = tk.Label(self.frame_b,text=f"{plist[h].score}",height=2,font=("Helvetica",12))
            score.grid(row=h+1,column=1)

            turn = tk.Label(self.frame_b,text=f"{'◄' if plist[h].myturn else ' '} ",height=2,font=("Helvetica",12))
            turn.grid(row=h+1,column=2)



    def player_turn(self,plist,s,dlist): # player turn toggle function
        # p,d list player, deck list

        for i in range(len(plist)):
            if plist[i].myturn==True:   # if player turn
                plist[i].score += s  # adds score
                if  dlist[0][0].value=='J' and dlist[1][0].value=='J': # Wildcard "JJ"
                    # player doesnt lose turn
                    break
                plist[i].myturn= False  # loses turn
                if dlist[0][0].value=='K' and dlist[1][0].value=='K': # Wildcard "KK"
                    if i == (len(plist)-1):  # if last player
                        plist[1].myturn = True  # second player plays
                        break
                    if i == (len(plist)-2):  # if second last player
                        plist[0].myturn = True  # first player plays
                        break
                    else:
                        plist[i+2].myturn = True
                        break
                if i == (len(plist)-1):  # if last player
                    plist[0].myturn = True  # first player plays
                else:
                    plist[i+1].myturn = True
                break
        
        for h in range (len(plist)): #Players presentation refresh
            player = tk.Label(self.frame_b,text=f"{plist[h].name}",height=2,font=("Helvetica",12))
            player.grid(row=h+1,column=0)

            score = tk.Label(self.frame_b,text=f"{plist[h].score}",height=2,font=("Helvetica",12))
            score.grid(row=h+1,column=1)

            turn = tk.Label(self.frame_b,text=f"{'◄' if plist[h].myturn else ' '} ",height=2,font=("Helvetica",12))
            turn.grid(row=h+1,column=2)


    # Check if the game is over
    def check_win(self,players):
        s=0
        k=0
        winners=[]
        for i in range(0,len(self.ndeck.cards)):
           if self.ndeck.cards[i].open==True:
            s +=1

        if s==len(self.ndeck.cards): #finds top score
            for p in range(0,len(players)):
                if players[p].score>k:
                    k=players[p].score

            for i in range(0,len(players)): #add players with top score to winners list
                if players[i].score==k:
                    winners.append(players[i].name)
        
            if len(winners)==1:
                tk.messagebox.showinfo('information','GAME OVER!!! Winner is: '+ winners[0])
            else:
                 tk.messagebox.showinfo('information','GAME OVER!!! Draw between:' + str([name for name in winners])) #will make this better!


    def quit(self):
        print("Quiting game")

    def save_game(self): #file clearance if save already exists
        decksave = "decksave.pickle"
        empty_list = []
        players_save = "players_save.pickle"
        with open(decksave,'wb') as self.dbfile1:
            if os.path.getsize(decksave) > 0:
                pickle.dump(empty_list, self.dbfile1)
            pickle.dump(self.ndeck,self.dbfile1)
        self.dbfile1.close()
        with open(players_save,'wb') as self.dbfile2:
            if os.path.getsize(players_save) > 0:
                pickle.dump(empty_list, self.dbfile2)
            pickle.dump(players,self.dbfile2)
        self.dbfile2.close()
        print("Game saved")

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
        self.play(players)

players = []
interface = GUI()
# Code DUMP (don't delete may use later)
