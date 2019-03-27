class Clock:

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def __advance_time(self):
        self.second = self.second + 1
        if self.second == 60:
            self.minute = self.minute + 1
            self.second = 0
        if self.minute == 60:
            self.hour = self.hour + 1
            self.minute = 0
        if self.hour == 13:
            self.hour = 1

    def __display_time_hour(self):
        return self.hour

    def __display_time_minute(self):
        return self.minute

    def __display_time_second(self):
        return self.second

    def __str__(self):
        self.__advance_time()
        return 'The time is now: ' + str(self.__display_time_hour()) + ':' + str(self.__display_time_minute()) + ":" + str(self.__display_time_second())

def main():
    x = 0
    timer = Clock()
    while x < 50000:
        print(timer)
        x = x + 1

main()
