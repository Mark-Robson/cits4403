from creature import *
import random


class herbivore(creature):
	worldsize = 0
	
	def __init__(self,foodlevel,xco,yco,newspeed,species_id,childSize,healthySize,worldsize):
		super().__init__(foodlevel,xco,yco,newspeed,species_id,childSize,healthySize)
		self.worldsize = worldsize

	def addFood(amount):
		self.food += amount
	
	def randommove(self):
		minx = -1
		maxx = 1
		if(self.x_co-1<0):
			minx = 0
		if(self.x_co+1>self.worldsize-1):
			maxx = 0

		miny = -1
		maxy = 1
		if(self.y_co-1<0):
			miny = 0
		if(self.y_co+1>self.worldsize-1):
			maxy = 0

		self.x_co = random.randint(minx+self.x_co   ,maxx+self.x_co)
		self.y_co = random.randint(miny+self.y_co   ,maxy+ self.y_co) 

		# print(str(self.x_co)+"  "+str(self.y_co))

		return 1
	
	def nextmove(self):
		
		self.food=self.food-1
		return self.randommove()

	


	def caneat(self,foodid): # only eat grass
		if(foodid==-1):
			return true
		else:
			return false