# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date:
# Software/Program Reference Number: Homework Assignment 4
# Software/Program Brief Description: The program should ask for a file name 
#                                     and display the data in the file, before
#                                     calculating the total of the date, then
#                                     calculating the average of the data
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/08/04     First Version
# *********************************************************************************************************
# Variable Initialization

data_total = 0
data_average = 0
lines = 0

def main():
    # 1. Ask the user for the file name
    file_name = input("What is the name of the file you want to use:")

    # 2. Load the file
    read_file = open(file_name, 'r')

    # 3. Display the contents of the file
    file_contents = read_file.read()
    for line in file_contents
        lines = lines + 1
        data = file_contents.readline()
        print(lines,":", data)
        data_total = data_total + data
    print("The total sum of the data is:", data_total)
    
    #
    data_average = data_total/lines
    print("The average of the data is:", data_average)
    