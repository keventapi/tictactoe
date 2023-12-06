import random
from time import sleep
class game():
    def __init__(self):
        self.data = []
        self.data = [[[] for i in range(3)] for i in range(3)]
        self.played = []
        self.x = []
        self.y = []
        self.win_condition = [[1,2,3],
                              [4,5,6],
                              [7,8,9],
                              [1,4,7],
                              [2,5,8],
                              [3,6,9],
                              [1,5,9],
                              [3,5,7]]

    def display(self):
        for i in self.data:
            print(i)

    def put_play(self, location, play):
        if location <= 3 and location > 0:
            self.data[0][location-1] = play
        if location > 3 and location <= 6:
            self.data[1][location-1-3] = play
        if location > 6 and location <= 9:
            self.data[2][location-1-6] = play
        if play == 'x':
            self.x.append(location)
        else:
            self.y.append(location)

    def chck_winner(self):
        print(self.x, self.y)
        if len(self.x) >= 3:
            for y in self.win_condition:
                xwin = all(x in self.x for x in y)
                if xwin:
                    return True
        if len(self.y) >= 3:
            for y in self.win_condition:
                ywin = all(x in self.y for x in y)
                if ywin:
                    return False


                    
    def put_y(self):
        y = random.randint(1, 9)
        if len(self.x)+len(self.y) == 9:
            print('none has won')
            self.reset()
        if self.played.count(y) == 0:
           self.played.append(y)
           self.put_play(y, 'y')
        else:
            self.put_y()

    def reset(self):
        self.data = []
        self.data = [[[] for i in range(3)] for i in range(3)]
        self.played = []
        self.x = []
        self.y = []

    def main(self):
        while True:
            print(self.played)
            stats = self.chck_winner()
            print(stats)
            if stats == True:
                print('u won')
                self.reset()
            elif stats == False:
                print('u lost')
                self.reset()
            self.display()
            location = int(input('where do u wanna to play'))
            if location <= 9 and location > 0:
                if self.played.count(location) == 0:
                    self.played.append(location)
                    self.put_play(location, 'x')
                    self.put_y()
            self.display()
            self.x = sorted(self.x)
            self.y = sorted(self.y)
            sleep(0.5)

main = game()

main.main()