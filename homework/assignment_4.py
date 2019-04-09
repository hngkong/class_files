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

def main():

    data_total = 0
    data_average = 0
    line_num = 0
    # 1. Ask the user for the file name
    file_name = input("What is the name of the file you want to use: ")

    # 2. Load the file
    with open(str(file_name), 'r') as fp:
        for line_num, data in enumerate(fp):
            # 3. Display the contents of the file
            print("Line {}: {}".format(line_num, data))
            data_total = data_total + data

    # 4. Display the total of all the data
    print("The total sum of the data is:", data_total)
    
    # 5. Display the average of all the data
    data_average = data_total/line_num
    print("The average of the data is:", data_average)
    
main()