'''
-------------------------------------------------------------------------------
Name:         My_Blackjack.py
Author:       Brian Kingery
Created:      7/14/2016

Purpose:      Blackjack

Directions:   Shuffle up and deal
-------------------------------------------------------------------------------
'''

import random
import time
import winsound

##    soundDictionary
##
##    deal            = winsound.PlaySound('c:/windows/media/recycle.wav', winsound.SND_FILENAME)
##    hit             = winsound.PlaySound('c:/windows/media/Speech On.wav', winsound.SND_FILENAME)
##    stand           = winsound.PlaySound('c:/windows/media/Windows Error.wav', winsound.SND_FILENAME)
##    playerWins      = winsound.PlaySound('c:/windows/media/tada.wav', winsound.SND_FILENAME)
##    dealerWins      = winsound.PlaySound('c:/windows/media/Windows User Account Control.wav', winsound.SND_FILENAME)
##    push            = winsound.PlaySound('c:/windows/media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)

W = 0   # Win
L = 0   # Loss
P = 0   # Push

#SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
SUITS = ('c', 's', 'h', 'd')
CARDS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

DECK = []

def ShuffleDeck():
    print "\n----------Shuffling----------\n"
    deal            = winsound.PlaySound('c:/windows/media/recycle.wav', winsound.SND_FILENAME)
    deal            = winsound.PlaySound('c:/windows/media/recycle.wav', winsound.SND_FILENAME)
    deal            = winsound.PlaySound('c:/windows/media/recycle.wav', winsound.SND_FILENAME)
    for suit in SUITS:
        for card in CARDS:
            DECK.append(card+suit)
    random.shuffle(DECK)
    time.sleep(1)

def DECK_Check(c,Pcards,Dcards):
    CARDS = len(DECK)
    print "Cards:",CARDS
    if CARDS >= 5:
        DECK.remove(c)
    elif CARDS < 5: # Shuffle if card count is less than 5 cards
        ShuffleDeck()
        if len(Pcards) > 0:
            for x in Pcards:
                DECK.remove(x)
        if len(Dcards) > 0:
            for x in Dcards:
                DECK.remove(x)

def printPlayerHand(Hand, score):
    print "\nPlayer's Hand"
    for c in Hand:
        print c,
    print "\nScore"
    print score,"\n"
    
def printDealerHand(Hand, score):
    print "\nDealer's Hand"
    for c in Hand:
        print c,
    print "\nScore"
    print score,"\n"

def printDealerHand_Beginning(Hand, score):
    print "\nDealer's Hand"
    if Hand[1][0] == 'A':
        score = 11
    else:
        score = VALUES[Hand[1][0]]
    print '--',Hand[1]
    print "Score"
    print score,'\n'

def printDealerHand_Partial(Hand, score):
    scoreTotal = 0
    print "\nDealer's Hand"
    if Hand[1][0] == 'A':
        score = 11
    else:
        score = VALUES[Hand[1][0]]
    HAND = Hand             # Creates a new list to remove the first card
    HAND.remove(Hand[0])
    print '--',
    for c in HAND:
        print c,
    for c in HAND:
        y = VALUES[c[0]]
        scoreTotal+=y
    print "\nScore"
    print scoreTotal,'\n'
        
def Intro():
    print "My_Blackjack.py\n"
    print "Rules:"
    print "1 - Cards are shuffled are dealt to Player and Dealer. Only one Dealer card is reveiled to Player."
    print "2 - Player can hit or stand until desired score is reached"
    print "    - Aces are counted as 1 unless dealt initially, then Ace = 11"
    print "    - If Player has Blackjack and Dealer does not, Player wins"
    print "    - If Player and Dealer both have Blackjack, Push"
    print "    - If Dealer has Blackjack, Dealer wins"
    print "3 - Dealer must continue to hit until score is greater than Player without going over 21"
    print "\nLet's play some BLACKJACK!\n"

def PLAY():
    print "="*30
    print "...........Dealing..........."
    print "="*30
    deal            = winsound.PlaySound('c:/windows/media/recycle.wav', winsound.SND_FILENAME)

    global W,L,P,PlayerHand,DealerHand,Dscore,Pscore,PscoreTotal
    PlayerHand = []
    DealerHand = []
    Dscore = 0
    Pscore = 0
    
    card = random.choice(DECK)                              # Deal inital cards
    PlayerHand.append(card)
    DECK_Check(card,PlayerHand,DealerHand)
    card = random.choice(DECK)
    DealerHand.append(card)
    DECK_Check(card,PlayerHand,DealerHand)
    card = random.choice(DECK)
    PlayerHand.append(card)
    DECK_Check(card,PlayerHand,DealerHand)
    card = random.choice(DECK)
    DealerHand.append(card)
    DECK_Check(card,PlayerHand,DealerHand)

    for card in DealerHand:                                 # Count hand values
        if VALUES[card[0]] == 1:
            x = 11
        else:
            x = VALUES[card[0]]
        Dscore+=x
    for card in PlayerHand:
        if VALUES[card[0]] == 1:
            x = 11
        else:
            x = VALUES[card[0]]
        Pscore+=x

    printPlayerHand(PlayerHand,Pscore)                      # Print hands
    printDealerHand_Beginning(DealerHand,Dscore)

    if Dscore == 21 and Pscore < 21:                        # Stop if Dealer has Blackjack
        print "Blackjack...Dealer Wins\n"
        print "Dealer's Hand"
        for c in DealerHand:
            print c,
        print "\nScore"
        print Dscore
        L+=1
        PlayAgain()
    elif Dscore == 21 and Pscore == 21:                     # Push if both have Blackjack
        print "PUSH"
        printDealerHand(DealerHand,Dscore)
        push            = winsound.PlaySound('c:/windows/media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
        P+=1
        PlayAgain()
    elif Dscore < 21 and Pscore == 21:                      # Stop if Player has Blackjack
        print "BLACKJACK! Player Wins!\n"
        printDealerHand(DealerHand,Dscore)
        playerWins      = winsound.PlaySound('c:/windows/media/tada.wav', winsound.SND_FILENAME)
        W+=1
        PlayAgain()
    elif Pscore < 21 or Pscore < PscoreTotal:
        HitStand(PlayerHand)

def HitStand(Hand):
    global PlayerHand,DealerHand,Pscore,card,L,PscoreTotal
    PscoreTotal = 0

    x = raw_input("Hit(1 or Enter) or Stand(2): ")
    if x == '1' or x == '':
        hit             = winsound.PlaySound('c:/windows/media/Speech On.wav', winsound.SND_FILENAME)
        card = random.choice(DECK)
        Hand.append(card)
        DECK_Check(card,PlayerHand,DealerHand)
        for c in Hand:
            i = VALUES[c[0]]
            PscoreTotal+=i
        printPlayerHand(PlayerHand,PscoreTotal)
        if PscoreTotal > 21:
            print "Busted...\n"                                  # If Busting while hitting
            printDealerHand(DealerHand,Dscore)
            L+=1
            PlayAgain()                                     
        elif PscoreTotal == 21:
            print "\nPlayer Stands with 21\n"
            DealerGO()
        else:
            HitStand(PlayerHand)
    elif x == '2':
        u = 0
        for c in Hand:
            if Hand[0][0] == 'A' and Hand[1][0] != 'A':
                i = 11
            elif Hand[0][0] != 'A' and Hand[1][0] == 'A':
                i = 11
            else:
                i = VALUES[c[0]]
            u+=i
        print "\nPlayer Stands with",u,"\n"
        stand           = winsound.PlaySound('c:/windows/media/Windows Error.wav', winsound.SND_FILENAME)
        DealerGO()

def DealerGO():
    global PlayerHand,DealerHand,Pscore,Dscore,card,L,W,PscoreTotal,DscoreTotal
    DscoreTotal = 0
    if (Dscore < Pscore or Dscore < PscoreTotal) and Dscore <= 17:
        hit             = winsound.PlaySound('c:/windows/media/Speech On.wav', winsound.SND_FILENAME)
        card = random.choice(DECK)
        DealerHand.append(card)
        DECK_Check(card,PlayerHand,DealerHand)
        for c in DealerHand:
            i = VALUES[c[0]]
            DscoreTotal+=i
        if (DscoreTotal < Pscore or DscoreTotal < PscoreTotal) and DscoreTotal <= 20: #<= 17:
            printDealerHand(DealerHand,DscoreTotal)
            DealerGO()
        elif DscoreTotal > 21:
            print "Dealer Busts...\n"                         # If Dealer Busts while hitting
            printDealerHand(DealerHand,DscoreTotal) 
            print "Player wins!"
            playerWins      = winsound.PlaySound('c:/windows/media/tada.wav', winsound.SND_FILENAME)
            W+=1
            PlayAgain()
    elif (Dscore >= Pscore or Dscore >= PscoreTotal) and Dscore <= 21:         # Dealer wins if same score as Player with 21 or under  
        print "Dealer wins"
        dealerWins      = winsound.PlaySound('c:/windows/media/Windows User Account Control.wav', winsound.SND_FILENAME)
        printDealerHand(DealerHand,Dscore)
        L+=1
        PlayAgain()
    elif (Dscore < Pscore or Dscore < PscoreTotal) and Dscore <= 21:
        printDealerHand(DealerHand,Dscore)
        DealerGO()

def PlayAgain():
    print "W:",W,
    print "L:",L,
    print "P:",P
    z = raw_input("Deal again?\nYes(1 or Enter) or No(2) ")
    if z == '1' or z == '':
        PLAY()
    elif z == '2':
        QUIT = raw_input("Thanks for playing!")
        quit

############################################################################################################
        
Intro()
ShuffleDeck()
PLAY()




























