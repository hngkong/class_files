# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: 3/12/2019
# Software/Program Reference Number: Objects Class
# Software/Program Brief Description: Teaching myself to create classes
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/26/03     First Version
# *********************************************************************************************************
# Variable Initialization

class Ball:

    def __init__(self):
        self.size = 10
        self.color = 1
        self.x_position = 5
        self.__y_position = 5
        self.x_speed = 1
        self.y_speed = 1

    def move(self):
        self.x_position = self.x_position + self.x_speed
        self.__y_position = self.x_position + self.y_speed
        print('The position is:', self.x_position,",", self.__y_position)
        self.bounce()

    def bounce(self):
        if self.__y_position > 10 or self.__y_position < 0:
            self.y_speed = self.y_speed * -1
        print('The y speed is now:', self.y_speed)
        if self.x_position > 10 or self.x_position < 0:
            self.x_speed = self.x_speed * -1

def main():
    x = 0
    bouncy = Ball()
    while x < 100:
        bouncy.move()
        x = x + 1
    print("Final X Position:", bouncy.x_position)
    while True:
        try:
            print(bouncy.y_position)
        except:
            print("That doesn't exist")

main()
