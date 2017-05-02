import numpy
from world import *

class randomworld(world):

	def __init__(self,mapsize):
		super().__init__(mapsize)
		self.mapsize = mapsize

	def addfood(self, amount):
		# print("we added "+str(amount)+" new food")
		for a in range(0,amount):
			x = random.randint(0,self.mapsize-1);
			y = random.randint(0,self.mapsize-1);
			self.foodmap[x][y] = self.foodmap[x][y] + 1

		self.totalfood = self.totalfood + amount

	def addamountfood(self,distrobuted, amount):
		# print("we added "+str(amount)+" new food")
		for a in range(0,int(amount/distrobuted)):
			x = random.randint(0,self.mapsize-1);
			y = random.randint(0,self.mapsize-1);
			self.foodmap[x][y] = self.foodmap[x][y] + distrobuted
		x = random.randint(0,self.mapsize-1);
		y = random.randint(0,self.mapsize-1);
		self.foodmap[x][y] = self.foodmap[x][y] + (amount%distrobuted)
		self.totalfood = self.totalfood + amount

