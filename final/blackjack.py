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
                # check win
                FirstPlayer.cash_available -= FirstPlayer.current_bet
                print("FirstPlayer.cash_available")

                FirstPlayer.want_to_bet = input("Do you want to continue?\ny/n? ")
        

        

main()