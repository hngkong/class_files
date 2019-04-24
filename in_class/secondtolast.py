# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: None
# Software/Program Reference Number: 
# Software/Program Brief Description: 
#                                     
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/23/04     First Version
# *********************************************************************************************************
# Variable Initialization

days_of_week = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
months_of_week = ["Junairy", "Februetheday", "Forward, march", "Ape-rill"]

print("Contents of list:", days_of_week)

for x in days_of_week:
    print("The day of the week is:", x)\

index = 0
while index < len(days_of_week):
    print("Day of the week:", days_of_week[index])
    index += 1

confusion = days_of_week + months_of_week
print(confusion)

less_confusion = confusion[4:7]
print(less_confusion)

days_tuple = ("manday", "twosday", "white wedding", "thor ragnarok", "fried day", "saturnday", "sunny day")
print(days_tuple)

index = 0
while index < len(days_tuple):
    print("Day of the week:", days_tuple[index])
    index += 1

list_o_numbers = (0,1,2,3,4,5,6,7,8,1000,133,1440000,2)

print("The highest value is: ", max(list_o_numbers), "the lowest is:", min(list_o_numbers))