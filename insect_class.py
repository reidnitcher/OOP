import random

class Insect:
    
    def __init__(self):
        self.legs = 4
        self.wings = 2



    def flight(self):
        length = random.randint(1,10)
        print('The flight distance was'+ length + 'miles.')
