from FoodRules import *

class CleanEater(FoodRules):

	def __init__(self):
		a =0

#returns (the amount of food to be left on the tile ,
 # the amount of food to be added back into the system later ) 
	def eat (self,creature,food_in_tile,max_size,max_stomach_size,speed):
		if(creature.stomach+food_in_tile<=max_stomach_size):
			creature.stomach = creature.stomach+food_in_tile
			return (0,0)
		else:
			food_in_tile = food_in_tile - (max_stomach_size-creature.stomach) 
			creature.stomach = max_stomach_size
			return (food_in_tile,0)
#returns (1 if dead from hunger 0 if not , amount of food to add back to system )
	def hunger(self,creature,min_size,speed):
		if   (creature.stomach >= speed):
			creature.stomach = creature.stomach - speed
			return (0,speed)
		else:
			amount_left = speed - creature.stomach
			creature.stomach = 0
			if(creature.size-2*amount_left >= min_size):
				creature.size = creature.size - 2*amount_left
				return (0,speed+amount_left)
			elif(creature.size-2*amount_left>=0):
				creature.size = creature.size -2*amount_left
				return (1,speed+amount_left)
			else:
				temp =  creature.size
				creature.size = 0
				return(1,speed-amount_left+temp)
	
	def grow(self,creature,grow_rate,max_size):
		if(creature.size < max_size):
			if(creature.stomach+creature.size <= max_size):
				creature.size = creature.size + creature.stomach
				creature.stomach = 0
				return 0
			else:
				old_size = creature.size
				creature.size = max_size
				creature.stomach = creature.stomach-(creature.size-old_size)
				return 0
		return 0

# returns the amount of food used to grow
	# def grow(self,creature,grow_rate,max_size):
	# 	if(creature.size < max_size):
	# 		if(creature.stomach >= 4*grow_rate):
	# 			creature.size = creature.size + grow_rate
	# 			creature.stomach = creature.stomach - 2*grow_rate
	# 			return grow_rate
	# 	return 0
