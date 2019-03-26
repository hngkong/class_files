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
        self.y_position = 5
        self.x_speed = .1
        self.y_speed = .1

    def move(self):
        self.x_position = self.x_position + self.x_speed
        self.y_position = self.x_position + self.y_speed

    def bounce(self):
        if self.y_position > 10 or self.y_position < 0:
            self.y_speed = self.y_speed * -1.05
            print(self.y_speed)

def main():
    x = 0
    bouncy = Ball()
    while x < 1000:
        bouncy.move()
        bouncy.bounce()
        x = x + 1

main()
