import numpy
import sys
import random

class WorldMap:
	total_food = int(0)
	mapsize = int(0)


	def __init__(self,size):
		self.total_food = 0
		self.mapsize = size
		
	def addFood(self , amount):
		self.total_food = self.total_food + amount

	def getTotalFood(self):
		return self.total_food

	def getfood(self , x , y):
		return self.total_food

	def removefood(self , x , y , amount):
		if(amount>self.total_food):
			print ("Error cant remove that amount of food")
		self.total_food = self.total_food - amount
		return amount

	def getSize(self):
		return self.mapsize

class SimpleSquare(WorldMap):
	foodmap = numpy.zeros((1,1))


	def __init__(self,mapsize):
		if(mapsize < 1):
			raise ValueError('Mapsize was '+ str(mapsize))
		self.foodmap = numpy.zeros((mapsize,mapsize))
		super().__init__(mapsize)

	def addFood(self, amount):
		for i in range(amount):
			x = random.randint(0,self.mapsize-1)
			y = random.randint(0,self.mapsize-1)
			self.foodmap[x][y] += 1
		self.total_food += amount

	def getfood(self , x , y):
		return self.foodmap[x][y]

	def removefood(self , x , y , amount):
		if(amount>self.foodmap[x][y]):
			print ("Error cant remove that amount of food")
		self.foodmap[x][y]-= amount
		self.total_food   -= amount


	def print_map(self):
		for i in range(self.mapsize):
			for j in range(self.mapsize):
				sys.stdout.write(('%5s ' % (str(self.foodmap[i][j])) ))
			sys.stdout.write('\n')
		sys.stdout.flush()
