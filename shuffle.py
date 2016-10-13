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
    time.sleep(0)

def DECK_Check(c,Pcards):
    CARDS = len(DECK)
    print "Cards:",CARDS
    if CARDS > 0:
        DECK.remove(c)
    if CARDS < 1:
        ShuffleDeck()
        for x in Pcards:
            DECK.remove(x)
        print len(DECK)

def PlayAgain():
    z = raw_input("Deal again?\nYes(1 or Enter) or No(2) ")
    if z == '1' or z == '':
        PLAY()
    elif z == '2':
        QUIT = raw_input("Thanks for playing!")
        quit

def PLAY():
    
    #global W,L,P,PlayerHand,DealerHand,Dscore,Pscore,PscoreTotal
    PlayerHand = []
    
    card = random.choice(DECK)                              # Deal inital cards
    PlayerHand.append(card)
    DECK_Check(card,PlayerHand)
    PlayAgain()
      
####################################################    

ShuffleDeck()
PLAY()
