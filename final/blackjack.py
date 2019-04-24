# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: May 7th?
# Software/Program Reference Number: Final Project
# Software/Program Brief Description: Blackjack
#                                     ...but no hookers
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/23/04     First Version
# *********************************************************************************************************
# Variable Initialization

import random

class Player:
    cash_available = 1000
    name = "default"
    current_bet = 0
    want_to_bet = 'y'

    def changeName(self):
        self.name = input("What is your name? ")

    def displayCash(self):
        print("You have", self.cash_available, "dollars.")

    def newBet(self):
        self.current_bet = float(input("How much would you like to bet? "))

class Cards:
    deck = [["Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts","Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds","Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs","Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"],[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]]

def main():
    print("Welcome!")
    FirstPlayer = Player()
    FirstPlayer.changeName()
    print("Welcome to the casino", FirstPlayer.name)

    FirstPlayer.displayCash()

    while FirstPlayer.want_to_bet == 'y' and FirstPlayer.cash_available > 0:
        FirstPlayer.newBet()
        if FirstPlayer.cash_available > FirstPlayer.current_bet:
            confirmation = str("You want to bet %s dollars? You have %s dollars available.\nType y to comnfirm:" % (FirstPlayer.current_bet, FirstPlayer.cash_available))
            print(confirmation)
            confirm_bet = input("y/n? ")
            if confirm_bet == 'y':
                # randomize cards
                # check win/loss
                FirstPlayer.cash_available -= FirstPlayer.current_bet
                print("FirstPlayer.cash_available")

                FirstPlayer.want_to_bet = input("Do you want to continue?\ny/n? ")
        

        

main()