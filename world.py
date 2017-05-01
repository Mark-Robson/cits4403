import numpy
import random


class world:

    foodmap = numpy.zeros((1, 1))
    totalfood = 0
    mapsize = 0

    def __init__(self, mapsize):
        if(mapsize < 1):
            raise ValueError('Mapsize was ' + str(mapsize))
        self.foodmap = numpy.zeros((mapsize, mapsize))
        self.mapsize = mapsize

    def addfood(self, amount):
        self.foodmap[0][0] += amount
        self.totalfood += amount

    def getTotalFood(self):
        return totalfood

    def getfood(self, x, y):
        if(x < 0 or y < 0 or x > self.mapsize or y > self.mapsize):
            raise ValueError('Mapsize was ' + str(mapsize) + " position " +
                             str(x) + "," + str(y) + " is not valid")
        return self.foodmap[x][y]

    def removefood(self, x, y):
        if(x < 0 or y < 0 or x > self.mapsize or y > self.mapsize):
            raise ValueError('Mapsize was '+str(mapsize) + " position " +
                             str(x) + "," + str(y) + " is not valid")
        temp = self.foodmap[x][y]
        self.foodmap[x][y] = 0
        self.totalfood -= temp
        return temp

    def getSize(self):
        return self.mapsize
