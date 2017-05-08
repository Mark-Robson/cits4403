# from sets import *
from Creature import *
from RandomMovement import *
from DeathRules import *
from CleanEater import *
from SingleChild import *
from WorldMap import *
from SimpleSquare import *
from RandomFoodSystem import *

class Species:
	species_id = 0

	population = 0
	deaths_laststep = 0
	births_laststep = 0 

	max_size = 0
	min_size = 0
	max_stomach_size = 0
	grow_rate = 0
	kid_size = 0
	kid_stomach_size = 0

	speed = 0
	members = []
	can_eat_list = []
	
	movement_system = MovementSystem()
	eating_rules = FoodRules()
	child_rules = ChildRules()
	death_rules = DeathRules()

	def __init__(self,movement_system,eating_rules,child_rules,death_rules,species_id,can_eat_list,max_size,min_size,max_stomach_size,grow_rate,kid_size,kid_stomach_size,speed):
		self.species_id = species_id
		self.can_eat_list= set(can_eat_list)
		self.max_size = max_size
		self.min_size = min_size
		self.max_stomach_size = max_stomach_size
		self.kid_size = kid_size
		self.kid_stomach_size = kid_stomach_size
		self.speed = speed
		self.grow_rate = grow_rate
		self.movement_system = movement_system
		self.eating_rules = eating_rules
		self.child_rules = child_rules
		self.death_rules = death_rules

	def getfoodsize(self,i):
		return (self.members[i].size , self.members[i].stomach)

	def totalMass(self):
		total = 0
		for i in self.members:
			total = total + i.getMass()
		return total
#returns (x,y) wasmove to
	def move(self,i,data):
		return self.movement_system.move(self.members[i],self.speed,data)

#returns (the amount of food to be left on the tile , the amount of food to be added back into the system later ) 
	def eat(self,i,food_in_tile):
		return self.eating_rules.eat(self.members[i],food_in_tile,self.max_size,self.max_stomach_size,self.speed)

#returns (1 if dead from hunger 0 if not , amount of food to add back to system )
	def hunger(self,i):
		return self.eating_rules.hunger(self.members[i],self.min_size,self.speed)

# retunrs the amout of food to add back into the system
	def grow(self, i):
		return self.eating_rules.grow(self.members[i],self.grow_rate,self.max_size)

# note that id 0 is grass
# note that id 1 is Meat on ground
# hunnting rule can be added here
	def can_eat(self,species_id):
		return species_id in self.can_eat_list

# simple list of id to kill returns the food to add to the system
#  at a list of (x,y,amount)
#  for x or y = -1 add randomly 
# TODO MAKE THIS MEAT NOT GRASS
	def Hunger_kill_members(self,alist):
		alist.sort()
		self.deaths_laststep = len(alist)
		self.population = self.population - len(alist)
		total = []
		for i in reversed(alist):
			# print("deleted a number"+str(i))
			if(i>=0):
				total = total+(self.death_rules.hunger(self.members[i]))
				#this may not work right
				del self.members[i]
		return total
# list of (x,y) locations to make a new member
	def add_members(self,alist):
		self.births_laststep = len(alist)
		self.population = self.population + len(alist)
		for i in alist:
			self.members.append(Creature(i[0],i[1],self.kid_size,self.kid_stomach_size))

#returns a list of x, y or kids if can not have a kid it is of size 0
	def havekid(self,i):
		return self.child_rules.havekid(self.members[i],self.max_size,self.min_size,self.kid_size,self.kid_stomach_size,0)
		
	def printmembers(self):
		for i in self.members:
			print(i.toString())