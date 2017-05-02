import numpy
from world import *

class randomworld(world):

	def __init__(self,mapsize):
		super().__init__(mapsize)
		self.mapsize = mapsize

	def addfood(self, amount):

		for a in range(0,amount):
			self.foodmap[random.randint(0,self.mapsize-1)][random.randint(0,self.mapsize-1)] += 1

		self.totalfood += amount
