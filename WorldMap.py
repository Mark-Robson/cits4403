import numpy
import sys
import random

class WorldMap:
    # This is a superclass for simplesquare. Check with mark if you need to know
    # anything, but it shouldn't be necessary

    def __init__(self, size):
        self.total_food = 0
        self.mapsize = size

    def addFood(self, amount):
        self.total_food = self.total_food + amount

    def getTotalFood(self):
        return self.total_food

    def getfood(self, x, y):
        return self.total_food

    def removefood(self, x, y, amount):
        if(amount > self.total_food):
            print("Error cant remove that amount of food")
        self.total_food = self.total_food - amount
        return amount

    def getSize(self):
        return self.mapsize


class SimpleSquare(WorldMap):
    
    # Inits based on the size of the map. N*N sized square.
    def __init__(self, mapsize):
        if(mapsize < 1):
            raise ValueError('Mapsize was ' + str(mapsize))
        self.foodmap = numpy.zeros((mapsize, mapsize))
        super().__init__(mapsize)

    # This is how you add new food to the map.
    def addFood(self, amount):
        # TODO: Improve speed
        for i in range(amount):
            x = random.randint(0, self.mapsize-1)
            y = random.randint(0, self.mapsize-1)
            self.foodmap[x][y] += 1
        self.total_food += amount

    def getfood(self, x, y):
        return self.foodmap[x][y]

    def removefood(self, x, y, amount):
        if(amount > self.foodmap[x][y]):
            print("Error cant remove that amount of food")
        self.foodmap[x][y] -= amount
        self.total_food -= amount

    def print_map(self):
        for i in range(self.mapsize):
            for j in range(self.mapsize):
                sys.stdout.write(('%5s ' % (str(self.foodmap[i][j]))))
            sys.stdout.write('\n')
        sys.stdout.flush()
