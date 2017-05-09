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

	def simpleLargeHerbfaster(number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()
		# (self,movement_system,eating_rules,child_rules,death_rules,species_id,can_eat_list,
		#  max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed):
		max_size = 50
		min_size = 10
		max_stomach_size = 3000
		grow_rate = 10
		kid_size = 10
		kid_stomach_size = 10
		speed = 2
		a = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed)
		
		alist = []
		for i in range(number):
			x = randint(0,world_size-1) 
			y = randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		a.add_members(alist)
		return a

	def simplesmallHerb(number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()
		# (self,movement_system,eating_rules,child_rules,death_rules,species_id,can_eat_list,
		#  
		max_size = 50
		min_size = 5
		max_stomach_size = 3000
		grow_rate = 10
		kid_size = 10
		kid_stomach_size = 0
		speed = 1
		a = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed)
		
		alist = []
		for i in range(number):
			x = randint(0,world_size-1) 
			y = randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		a.add_members(alist)
		return a

	def simplesmallHerbfast(number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()
		# (self,movement_system,eating_rules,child_rules,death_rules,species_id,can_eat_list,
		#  
		max_size = 50
		min_size = 5
		max_stomach_size = 3000
		grow_rate = 10
		kid_size = 10
		kid_stomach_size = 0
		speed = 10
		a = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed)
		
		alist = []
		for i in range(number):
			x = randint(0,world_size-1) 
			y = randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		a.add_members(alist)
		return a

	def verysmallHerbfast(number,world_size,id,can_eat_list):
		food_law  = CleanEater()
		death_law = DeathRules()
		movement_law= RandomMovement(world_size)
		child_rule = SingleChild()
		# (self,movement_system,eating_rules,child_rules,death_rules,species_id,can_eat_list,
		#  
		max_size = 6
		min_size = 1
		max_stomach_size = 5
		grow_rate = 10
		kid_size = 2
		kid_stomach_size = 1
		speed = 10
		a = Species(movement_law,food_law,child_rule,death_law,id,can_eat_list,max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed)
		
		alist = []
		for i in range(number):
			x = randint(0,world_size-1) 
			y = randint(0,world_size-1) 
			alist.append((x,y))
		# list of (x,y) locations to make a new member
		a.add_members(alist)
		return a