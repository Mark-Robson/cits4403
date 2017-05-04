import numpy
from WorldMap import *

class SimpleSquare(WorldMap):
	foodmap = numpy.zeros((1,1))


	def __init__(self, FoodSystem , size):
		if(mapsize < 1):
			raise ValueError('Mapsize was '+ str(mapsize))
		self.foodmap = numpy.zeros((mapsize,mapsize))
		super().__init__(FoodSystem , mapsize)

	def addfood(self, amount):
		if(amount>__mapsize):
			add = self.FoodSystem.addfood(amount)
		else:
			add = self.FoodSystem.addLargeFood(amount)
		for a in add:
			self.foodmap[a[0]][a[1]] = self.foodmap[a[0]][a[1]] + a[2]
		self.__total_food = self.__total_food + amount

	def getfood(self , x , y):
		return self.foodmap[x][y]

# This will try to remove amount food for tile at x, y returning the amount of 
# food that was removed 
	def removefood(self , x , y , amount):
		if(amount>self.foodmap[x][y]):
			amount = self.foodmap[x][y]
			foodmap[x][y] = 0
			self.__total_food = self.__total_food - amount
			return amount
		self.foodmap[x][y] = self.foodmap[x][y] - amount
		self.__total_food = self.__total_food - amount
		return amount
