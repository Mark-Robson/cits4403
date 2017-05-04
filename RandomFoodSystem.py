from FoodSystem import *
import random

class RandomFoodSystem(FoodSystem):
	random_number_seed = 0
	random_number_gen
	world_size = 0
	def __init__(self,world_size,**keywordArgs):

		self.world_size = world_size
		for i in keywordArgs:
			if(i == "Random_number_seed" ):
				self.random_number_seed = keywordArgs.get(i)
				random.seed(self.random_number_seed);
			else:
				raise ValueError("keyword "+i+'''is unknowen
				the knowen keyworeds are:
				Random_number_seed''')
		random_number_gen = random.getState()


	def addFood(self,amount):
		a = []
		random.setState(self.random_number_gen)
		for i in amount:
			x = random.randint(0,self.mapsize-1)
			y = random.randint(0,self.mapsize-1)
			a.append((x,y,1))
		self.random_number_gen = random.getState()
		return a

