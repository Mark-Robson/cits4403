from MovementSystem import *
import random

class RandomMovement(MovementSystem):
	world_size = 0
	def __init__(self,world_size):
		self.world_size = world_size
		

	def move (self,creature,speed,data):
		minx = creature.x-speed
		maxx = creature.x+speed
		if(creature.x-speed<0):
			minx = 0
		if(creature.x+speed>self.world_size-1):
			maxx = self.world_size-1

		miny = creature.y-speed
		maxy = creature.y+speed
		if(creature.y-speed<0):
			miny = 0
		if(creature.y+speed>self.world_size-1):
			maxy = self.world_size-1

		creature.x = random.randint(minx  ,maxx)
		creature.y = random.randint(miny  ,maxy) 

		return creature.x,creature.y
