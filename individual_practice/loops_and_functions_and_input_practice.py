# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date:
# Software/Program Reference Number: Class Discussion 2ish
# Software/Program Brief Description: Write a hot goddamn mess of a program
#                                     that does loops, functions, maybe ifs?
#
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/??/??     First Version
# *********************************************************************************************************
# Variable Initialization


# Step 1: Define a function main
def main():
    # Step 1.5: What needs to happen in main()?
    # First define variables with scope of main
    hate_count = 0
    keep_going = 'y'
    hot_mess = int(input("How many times do I want to die?"))
    # First point five do an if statement
    if hot_mess >= 1:
        # Second, run the loop determining if I still hate myself
        while keep_going == 'y':
            # I still hate myself, so let's count up the hate
            hate_count = hate_count + 1
            print("\nEvery day I pray for the sweet release of death.")
            # Set a counting variable
            x = 1
            # World's worst while loop
            while x < 10:
                print("I wish I was dead")
                x = x + 1
            # Get the amount of ways I hate myself to loop in the for loop
            z = int(input("How many ways do I hate myself? "))
            for y in range(z):
                print("I hate", y + 1, "things about myself")
            # Do I still hate myself?  I mean, obviously, but do I want to keep reveling in it?
            keep_going = input("Do I still hate myself? ")
            print(keep_going)
        # How many times did I hate on myself today?
        print("I have been through this", hate_count, "times")
    else:
        print("Nice. Good day.")

# Step 2: Call main()
main()
