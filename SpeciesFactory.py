from Species import *
from RandomMovement import *
from DeathRules import *
from CleanEater import *
from SingleChild import *
class SpeciesFactory:
	def __init__(self):

	def simpleLargeHerb(self,number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()

		Speciesa = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,
	50,10,30,10,10,10,1):
		
		alist = []
		for i in range(number):
			x = random.randint(0,world_size-1) 
			y = random.randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		Speciesa = add_members(alist):
		return Speciesa