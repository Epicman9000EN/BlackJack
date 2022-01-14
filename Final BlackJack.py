from tkinter import *
import random

canvas_h = 1200
canvas_w = 900

player_score = 0
dealer_score = 0

turn = False


class card:
    
    list_cards = []
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
        
    def __str__(self):
        return f"{self.value} of {self.suit}"



def cards():
    
    for x in range(13):
        if x == 0:
            value = "Ace"
        elif x == 10:
            value = "Jack"
        elif x == 11:
            value = "Queen"
        elif x == 12:
            value = "King"
        else:
            value = x + 1
        
        for y in range(4):
            if y == 0:
                suit = "diamonds"
            if y == 1:
                suit = "clubs"
            if y == 2:
                suit = "hearts"
            if y == 3:
                suit = "spades"
    
            card.list_cards.append(card(suit, value))

def restart(root):
    global player_score
    global dealer_score
    
    card.list_cards = []
    player_score = 0
    dealer_score = 0
    root.destroy()
    start()


def ui(root, user_interface):
    global turn
    
    if player_score > 21:
        user_interface.config(text="Player Busted!!\n      Dealer Wins!!     ")
        turn = True
            
def player_cards(root, player_score_frame, dealer_score_frame, random_card):
    
    unicode1 = "\u2666"
    unicode2 = "\u2663"
    unicode3 = "\u2665"
    unicode4 = "\u2660"
    
    colnum = 53 - len(card.list_cards)
    
    if random_card.suit == "diamonds":
        if random_card.value == "Ace":
            random_card.value = "A"
            card_label = Label(player_score_frame, text=f"{random_card.value}{unicode}")
            card_label.grid(colnum = 1, row = 0)
        elif random_card.value == "Jack":
            random_card.value = "J"
            card_label = Label(player_score_frame, text=f"{random_card.value}{unicode}")
            card_label.grid(column = 1, row = 0)
        elif random_card.value == "Queen":
            random_card.value = "Q"
            card_label = Label(player_score_frame, text=f"{random_card.value}{unicode}")
            card_label.grid(column = 1, row = 0)
        elif random_card.value == "King":
            random_card.value = "K"
            card_label = Label(player_score_frame, text=f"{random_card.value}{unicode}")
            card_label.grid(column = 1, row = 0)
        
    elif random_card.suit == "clubs":
        random_card.value = 10
    elif random_card.suit == "hearts":
        random_card.value = 10
    elif random_card.suit == "spades":
        random_card.value = 10
    
            
def draw(player_count, root, user_interface, player_score_frame, dealer_score_frame):
    global player_score
    global turn
    
    if turn != True:     
        
        random_card = random.choice(card.list_cards)
        
        player_cards(root, player_score_frame, dealer_score_frame, random_card)
        
        if random_card.value == "Ace":
            random_card.value = 1
        elif random_card.value == "Jack":
            random_card.value = 10
        elif random_card.value == "Queen":
            random_card.value = 10
        elif random_card.value == "King":
            random_card.value = 10
            
        player_score += int(random_card.value)
        res = "Player Score: " + str(player_score)
        player_count.config(text=res)
        
        if player_score > 21:
            ui(root, user_interface)            
            
        
        
def dealer(card_obj1,root):
    global turn
    turn = True
    

def buttons(root, player_count, user_interface, button_frame, player_score_frame, dealer_score_frame):
    
    global turn
    
    if turn != True:
        card_frame = Frame(button_frame)
        card_frame.grid(column = 0, row = 0)
        
        card_obj1 = Button(card_frame, text="  Hit  ", font=("Times New Roman", 20, "bold"), padx = 40, pady = 40, command = lambda: draw(player_count, root, user_interface, player_score_frame, dealer_score_frame))
        card_obj2 = Button(card_frame, text="Stand", font=("Times New Roman", 20, "bold"), padx = 40, pady = 40, command = lambda: dealer(card_obj1, root))
        
        card_obj1.grid(column = 0, row = 0)
        card_obj2.grid(column = 0, row = 1)


def score(root, player_score_frame, dealer_score_frame):
    global player_score
    global dealer_score
    
    player_count = Label(player_score_frame, text="Player Score: " + str(player_score), font=("Times New Roman", 20, "bold"))
    dealer_count = Label(dealer_score_frame, text="Dealer Score: " + str(dealer_score), font=("Times New Roman", 20, "bold"))
    
    player_count.grid(column = 0, row = 0)
    dealer_count.grid(column = 0, row = 2)

    return player_count


def main(root):
    
    player_score_frame = Frame(root)
    player_score_frame.pack()
    
    dealer_score_frame = Frame(root)
    dealer_score_frame.pack()
    
    button_frame = Frame(root)
    button_frame.pack()
    
    user_interface = Label(button_frame, text="Click 'Hit' to\ndraw a card.\nClick 'stand' to stay", font=("Times New Roman", 20, "bold"), pady = 40)
    user_interface.grid(column = 1, row = 0)
    
    new_game = Button(root, text="New Game", font=("Times New Roman", 15, "bold"), command = lambda: restart(root))
    quit_game = Button(root, text="Quit Game", font=("Times New Roman", 15, "bold"), command = lambda: quit())
    new_game.pack()
    quit_game.pack()
    
    cards()
    player_count = score(root, player_score_frame, dealer_score_frame)
    buttons(root, player_count, user_interface, button_frame, player_score_frame, dealer_score_frame)
    
    

def initialize(Nugget):    
    Nugget.destroy()
    root = Tk()
    Canvas(root, height=canvas_h, width=canvas_w)
    title = Label(root, text="BlackJack", font=("Times New Roman", 60, "bold"))
    title.pack()
    root.update()
    root.geometry("1200x900+200+50")
    main(root)
    root.mainloop()
    
    
def start():
    Nugget = Tk()
    start_label = Label(Nugget, text="Play?")
    button_yes = Button(Nugget,  width=40, text="Yes", command=lambda: initialize(Nugget))
    button_no = Button(Nugget, width=40, text="No", command=lambda: quit())
    Nugget.geometry("300x300+600+400")
    start_label.pack()
    button_yes.pack()
    button_no.pack()
    Nugget.mainloop()


start()