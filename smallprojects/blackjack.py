from random import randint
from IPython.display import clear_output
import time
from rich import print
class Blackjack ( ) :
    def __init__ (self):
        self.deck = [ ]  #set to empty list
        self.suits = ("Spades","Heart","Clubs","Diamonds")
        self.values = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")
    
    def makeDeck ( self ): # Create a deck of cards
        self.deck.clear( )
        for suit in self.suits :
            for value in self.values :
                self.deck.append ( (value,suit) ) # ex: (7, Heart)
                
    def shuffleDeck ( self ) :
        self.deck = [ ]
        self.makeDeck( )
        
    def pullCard ( self ):
        return self.deck.pop ( randint (0, len (self.deck) -1 ) )
        

class Player ( ) :
    def __init__ (self, name, currency =0):
        self.name = name
        self.hand = [ ]
        self.currency = currency
        self.wager = 0
        
    def addCard ( self,card ):
        self.hand.append (card)
        
    def clearHand ( self ) :
        self.hand.clear( )
    
    def getCurrency ( self ) :
        return int ( self.currency )
    
    def calcCurrency ( self, wager, winner = "") :
        self.wager = wager
        if winner == "dealer" :
            self.currency -= wager
        elif winner == "player" :
            self.currency += wager          
    
    def checkWager ( self, wager) :
        if ( wager > self.currency ) or ( wager <= 0 ) :
            return True
        
    def showHand ( self, dealer_start = True ):
        print ( f"\n{ self.name }", "=" * 10 )
        for i in range (len ( self.hand )) :
            if self.name == "Dealer" and i == 0 and dealer_start:
                print (" - of -") # Hide the first hand
            else:
                card = self.hand [ i ]
                print (f"{ card[ 0 ] } of { card[ 1 ] }")
        print (f"The total is { self.calcHand( dealer_start ) }")
        
    def calcHand ( self,dealer_start = True ) :
        total = 0
        aces = 0
        card_values = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "A":11, "Q":10, "K":10, "J":10}
        if dealer_start and self.name == "Dealer" :
            card = self.hand [1]
            return ( card_values [ card[0] ] )
        for card in self.hand :
            if card [0] == "A" :
                aces += 1
            else :
                total += card_values [ card[0] ]
        for i in range ( aces ) :
            if total + 11 > 21 :
                total += 1
            else :
                total += 11
        return total
                                                               
game = Blackjack ( )
try_again = True
while try_again :
    try :
        name, currency = input ("What is the player name and how much money you want to risk?").split()
        (int ( currency ) )
        try_again = False
        print (f"${ currency } is locked in the game!\n")
        time.sleep(3)
    except ValueError:
        print (f"Enter a Name and a Number, Try again!")
        time.sleep(3)
    finally :
        clear_output( )
        
player = Player ( name,int ( currency ) )
dealer = Player ("Dealer")
playing = "yes"
while playing != "quit" and ( player.getCurrency( ) > 0 ):
    clear_output( )
    print ( f" You have { player.getCurrency ( )} in reserve!\n", "=" * 40, "\n" )
    wager = int ( input (f"What is this round wager?") ) 
    while player.checkWager (wager) :
        wager = int ( input (f"Wager should be less than { player.getCurrency( ) }! What is this round wager?") )
    clear_output( )    
    print ( f"${ wager } is on the tabele\n", "=" * 30 )
    game.makeDeck( )
    player.clearHand( )
    dealer.clearHand( )
    for i in range (2):
        player.addCard ( game.pullCard( ) )
        dealer.addCard ( game.pullCard( ) )
    player.showHand( )
    dealer.showHand( )

    player_bust = False  # variable to keep track of player going over 21
    while input ( "Would you like to stay or hit?" ).lower( ) != "stay" :
        clear_output()
        player.addCard ( game.pullCard ( ) )
        player.showHand ( )
        dealer.showHand ( )
        if player.calcHand ( ) > 21 :
            player_bust = True  # player busted, keep track for later
            print ("You lost!")  # remove after running correctly
            break  # break out of the player's loop
        
    # handling the dealer's turn, only run if player didn't bust
    dealer_bust = False
    if not player_bust:
        while dealer.calcHand (False) < 17 :
            dealer.addCard (game.pullCard ())
            if dealer.calcHand (False) > 21:
                dealer_bust = True
                print ("You Won!")
                break

    clear_output()
    player.showHand()
    dealer.showHand(False)
    if player_bust :
        player.calcCurrency (wager, "dealer")
        print("You busted, better luck next time!")
    elif dealer_bust :
        player.calcCurrency (wager, "player")
        print("The dealer busted, you win!")
    elif dealer.calcHand (False) > player.calcHand () :
        player.calcCurrency (wager, "dealer")    
        print("Dealer has higher cards, you lose!")
    elif dealer.calcHand (False) < player.calcHand () :
        player.calcCurrency (wager, "player")        
        print("You beat the dealer! Congrats!")
    else :
        print("You pushed, no one wins!")
    playing = input ("Type 'quit' if you want to leave:").lower()

if player.getCurrency ( ) <= 0 :
    print ("=" * 40,f"\nYou do not have enough fund! {player.getCurrency( )}\n")    
            