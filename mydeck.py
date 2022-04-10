import random
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

class Card:
    def __init__(self,suit,value,id):
        self.suit=suit
        self.value=value
        self.id=id
        self.open= True # Ανοιχτή/Κλειστή

    def show(self):
        if self.open==False:
            print("id:",self.id," XX")
        else:
            print("id:",self.id,"{}{}".format(self.value,self.suit))

class Deck:
    def __init__(self,difficulty):
        self.cards=[]
        self.build(difficulty)
        self.shuffle()

    def build(self,diff_choice):
        id=0
        if diff_choice=='easy':    
            for s in ["♠","♣","♦","♥"]:
                for v in (10,'J','Q','K'):
                    id=id+1
                    self.cards.append(Card(s,v,id))
        elif diff_choice=='average':
            for s in ["♠","♣","♦","♥"]:
                for v in (1,2,3,4,5,6,7,8,9,10):
                    id=id+1
                    self.cards.append(Card(s,v,id))
        elif diff_choice=='hard':
            for s in ["♠","♣","♦","♥"]:
                for v in (1,2,3,4,5,6,7,8,9,10,'J','Q','K'):
                    id=id+1
                    self.cards.append(Card(s,v,id))

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
        self.root = tk.Tk()
        self.root.geometry("400x300") # Μεγεθος παραθυρου
        self.root.resizable(0,0) # Κανει το παραθυρο να μην επεκτεινεται
        self.cards = []
        self.build()

    def build(self):
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#8cd921')  #
        # Κουμπια
        play_btn = ttk.Button(self.root,text="Play",command=self.play,style='A.TButton')
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
        self.root.resizable(0,0)
        card_id = 0
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,), foreground="red")
        style.configure('B.TButton', font=('Helvetica',12,), foreground="black")
        style.configure('Hidden.TButton',font=('Helvetica',20))
        frame = ttk.Frame(width=300,height=300)
        for i in range(4):
            for j in range (4):
                # Test Drive Cards
                # if test.cards[card_id].suit in ["♦","♥"]:
                #     card = ttk.Button(self.root,text=f"{test.cards[card_id].value}{test.cards[card_id].suit}",style="A.TButton")
                # else:
                #     card = ttk.Button(self.root,text=f"{test.cards[card_id].value}{test.cards[card_id].suit}",style="B.TButton")
                card = tk.Button(self.root,text="🂠",height=3,width=5,font=("Helvetica"),command=lambda i=i,j=j:self.select_card(i,j))
                # remove i=i j=j to see late binding issue
                # lamda για περασμα arguments
                card.grid(row=i,column=j)
                card_id += 1
        self.root.mainloop()


    def select_card(self,row,col):
        # κωδικας για επιλογη καρτας
        print(row,col)

    def select_players(self):
        #  Under construction
        self.root.destroy()  # Διαγραφη παραθυρου μενου
        self.root = tk.Tk()  # Εκκινηση παραθυρου παιχνιδιου
        self.root.geometry("300x400")
        self.root.resizable(0,0)
        self.root.title("Cards Game")  # Τιτλος παραθυρου
        style = ttk.Style() # Δημιουργια Στυλ
        style.theme_use('alt')
        style.configure('A.TButton', font=('Helvetica',12,),  background='#111111')
        player1 = ttk.Button(self.root, text="1 Player", command=self.action_select_players)
        player2 = ttk.Button(self.root, text="2 Players", command=self.action_select_players)
        player3 = ttk.Button(self.root, text="3 Players", command=self.action_select_players)
        player4 = ttk.Button(self.root, text="4 Players", command=self.action_select_players)
        player1.grid(row=0,column=0,ipadx=50,ipady=20,padx=63,pady=10)
        player2.grid(row=1,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        player3.grid(row=2,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        player4.grid(row=3,column=0,ipadx=50,ipady=20,padx=30,pady=10)
        self.root.mainloop()

    def action_select_players(self,num):
        #  Under construction
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
test.show_deck()
interface = GUI()