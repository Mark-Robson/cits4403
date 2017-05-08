import numpy
import sys
from WorldMap import *

class SimpleSquare(WorldMap):
	foodmap = numpy.zeros((1,1))


	def __init__(self, FoodSystem , mapsize):
		if(mapsize < 1):
			raise ValueError('Mapsize was '+ str(mapsize))
		self.foodmap = numpy.zeros((mapsize,mapsize))
		super().__init__(FoodSystem , mapsize)

	def addFood(self, amount):
		add = []
		add = add + self.food_system.addFood(amount)
		# print("WHY !!!! "+add)
		for a in add:
			# print(str(a[0])+"  "+str(a[1])+"  "+str(a[2])+"  ")
			self.foodmap[a[0]][a[1]] = self.foodmap[a[0]][a[1]] + a[2]
		self.total_food = self.total_food + amount

	def getfood(self , x , y):
		return self.foodmap[x][y]

# This will try to remove amount food for tile at x, y returning the amount of 
# food that was removed 
	def removefood(self , x , y , amount):
		# sprint(str(self.total_food)) 
		if(amount>self.foodmap[x][y]):
			k = self.foodmap[x][y]
			foodmap[x][y] = 0
			self.total_food = self.total_food - k
			return k
		self.foodmap[x][y] = self.foodmap[x][y] - amount
		self.total_food = self.total_food - amount
		return amount


	def print_map(self):
		for i in range(self.mapsize):
			for j in range(self.mapsize):
				sys.stdout.write(('%5s ' % (str(self.foodmap[i][j])) ))
			sys.stdout.write('\n')
		sys.stdout.flush()		

