# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date:
# Software/Program Reference Number: Class Discussion 3ish
# Software/Program Brief Description: Write a hot goddamn mess of a program
#                                     that fucks with files.
#
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/??/??     First Version
# *********************************************************************************************************
# Variable Initialization

# open('file', 'a/r/w')  # a means to append, or add to the end of the file
                         # r means to read, no data is changed
                         # w means to write, which will overwrite any previous data if any exists
                       
outfile = open('philosophers.txt', 'a')  # outfile is the variable for the file

outfile.write('John Locke\n')
outfile.write('David Hume\n')
outfile.write('Heavy Metal Suicide\n')

outfile.close()

# delete above?, to do below  (as above, so below - lol)

infile = open('philosophers.txt', 'r')

file_contents = infile.read()  # read the whole file, set the stuff inside to file_contents, 
                               # as long as the program is still running, will not read any 
                               # contents again

print(file_contents)

line1 = infile.readline() # reads the first line, as long as the program is still running, will not read the line again
line2 = infile.readline() # as above, so below
line3 = infile.readline() # as above, so below
line4 = infile.readline() # as above, so below

print(line1) # will do nothing based on file_contents above having read everything.  Comment it out if you want it to work
print(line2)
print(line3)
print(line4)

infile.close()
