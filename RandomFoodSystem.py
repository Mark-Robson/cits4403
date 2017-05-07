from FoodSystem import *
import random

class RandomFoodSystem(Foodsystem):
	world_size = 0
	def __init__(self,world_size):
		self.world_size = world_size


	def addFood(self,amount):
		a = []
		for i in range(amount):
			x = random.randint(0,self.world_size-1)
			y = random.randint(0,self.world_size-1)
			a.append((x,y,1))
		return a

