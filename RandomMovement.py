from MovementSystem import *
class RandomMovement(MovementSystem):
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


	def move (self,creature,speed,data):
		minx = -1*speed
		maxx = speed
		if(creature.x-speed<0):
			minx = 0
		if(creature.x+speed>self.world_size-1):
			maxx = self.world_size-1

		miny = -1*speed
		maxy = speed
		if(creature.y-speed<0):
			miny = 0
		if(creature.y+speed>self.world_size-1):
			maxy = self.world_size-1

		creature.x = random.randint(minx+creature.x  ,maxx+creature.x)
		creature.y = random.randint(miny+creature.y  ,maxy+creature.y) 

		return creature.x,creature.y
