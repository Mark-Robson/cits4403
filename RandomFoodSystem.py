from FoodSystem import *
import random
import numpy
class RandomFoodSystem(Foodsystem):
	world_size = 0
	def __init__(self,world_size):
		self.world_size = world_size

	def addLargeFood(self,amount):
		m = numpy.zeros((self.world_size,self.world_size))
		for i in range(amount):
			x = random.randint(0,self.world_size-1)
			y = random.randint(0,self.world_size-1)
			m[x][y]= m[x][y]+1
		a = []
		for i in range(self.world_size):
			for j in range(self.world_size):
				a.append((i,j,m[i][j]))
		return a

	def addFood(self,amount):
		a = []
		if (amount >= self.world_size*self.world_size):
			return self.addLargeFood(amount)
		for i in range(int(amount/10)):
			x = random.randint(0,self.world_size-1)
			y = random.randint(0,self.world_size-1)
			a.append((x,y,1))
		x = random.randint(0,self.world_size-1)
		y = random.randint(0,self.world_size-1)
		a.append((x,y,amount%10))
		return a


