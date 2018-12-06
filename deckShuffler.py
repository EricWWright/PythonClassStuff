import random

deck = []
player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []

def makeDeck(deck):
    """ populate the deck of cards """
    SUITS = ("hearts", "dimonds", "clubs", "spades")
    VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)

def shuffleDeck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

def dealCard(deck,player1_hand,player2_hand,player3_hand,player4_hand):
    for i in range(5):
        card = deck.pop(0)
        player1_hand.append(card)
        card = deck.pop(0)
        player2_hand.append(card)
        card = deck.pop(0)
        player3_hand.append(card)
        card = deck.pop(0)
        player4_hand.append(card)

# makeDeck(deck)
# print(deck)
# print(len(deck))
# shuffleDeck(deck)
# print(deck)
# print(len(deck))
# dealCard(deck,player1_hand,player2_hand,player3_hand,player4_hand)
# print()
# print(player1_hand)
# print(player2_hand)
# print(player3_hand)
# print(player4_hand)