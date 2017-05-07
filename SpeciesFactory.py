from Species import *
from RandomMovement import *
from DeathRules import *
from CleanEater import *
from SingleChild import *
from random import *
class SpeciesFactory:
	def __init__(self):
		a=1

	def simpleLargeHerb(number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()

		a = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,50,10,30,10,10,10,1)
		
		alist = []
		for i in range(number):
			x = randint(0,world_size-1) 
			y = randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		a.add_members(alist)
		return a