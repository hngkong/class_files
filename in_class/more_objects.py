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
    InsectName = ""
    InsectWings = False

def main():
    HouseFly = Insect()
    Mosquito = Insect()
    Ant = Insect()

    HouseFly.InsectName = "House Fly"
    Mosquito.InsectName = "Mosquito"
    Ant.InsectName = "Ant"
    HouseFly.InsectWings = True

    print("The name of the HouseFly object InsectName is:",HouseFly.InsectName)
    print("A house fly has wings:",HouseFly.InsectWings)
    print("The name of the Ant object InsectName is:",Ant.InsectName)
    print("An ant has wings:",Ant.InsectWings)
    print("The name of the Mosquito object InsectName is:",Mosquito.InsectName)
    print("A dingo ate my baby:",Mosquito.InsectWings)

main()