# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: None, in class work
# Software/Program Reference Number: In Class Work
# Software/Program Brief Description: Honestly, I'm not sure anymore,
#                                     but I'm pretty sure it's arrays
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/16/04     First Version
# *********************************************************************************************************
# Variable Initialization

class Insect:

    def __init__(self):
        self.fuck_me = "No shit"
        self.this_sucks = 10
        print(self.fuck_me)

    def fuckThis(self):
        self.fuck_me = "This shit sucks"
        print(self.fuck_me)

def main():
    jack = Insect()

    jack.fuckThis()

main()