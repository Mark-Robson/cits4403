# from sets import *
from Creature import *
from WorldMap import *
import random
class Species:
	species_id = 0

	population = 0
	population_mass = 0
	min_size = 0
	kid_size = 0

	members = []
	can_eat_list = []
	
	world_size = int(0)
	map = WorldMap(1);

	def __init__(self,map,species_id,can_eat_list,min_size,kid_size):
		self.map = map
		self.species_id = species_id
		self.can_eat_list= set(can_eat_list)
		self.min_size = min_size
		self.kid_size = kid_size
		self.world_size = map.mapsize

	def getPopulationMass(self):
		return self.population_mass

	def getlocation(self,i):
		return self.members[i].x , self.members[i].y

	def stepSpecies(self):
		alist = []
		for i in range(self.population):
			self.move(i,1)
			if(self.hunger(i,1)):
				alist.append(i)
		self.Remove_killed_members(alist)
		newPop = []
		newPop = self.havekid()
		self.add_members(newPop)

	def move(self,i,speed):	
		minx = self.members[i].x-speed
		maxx = self.members[i].x+speed
		if(self.members[i].x-speed<0):
			minx = 0
		if(self.members[i].x+speed>self.world_size-1):
			maxx = self.world_size-1

		miny = self.members[i].y-speed
		maxy = self.members[i].y+speed
		if(self.members[i].y-speed<0):
			miny = 0
		if(self.members[i].y+speed>self.world_size-1):
			maxy = self.world_size-1

		self.members[i].x = random.randint(minx  ,maxx)
		self.members[i].y = random.randint(miny  ,maxy)

		if(0 in self.can_eat_list):
			self.eatgrass(i)


	def eatgrass(self,i):
		amount = self.map.getfood(self.members[i].x,self.members[i].y)
		self.map.removefood(self.members[i].x,self.members[i].y,amount)
		self.members[i].size+=amount
		self.population_mass+=amount
		
#returns 1 if dead from hunger 0 if not 
	def hunger(self,i,amount):
		self.members[i].size-=amount
		self.population_mass-=amount
		if(self.members[i].size<self.min_size):
			self.population_mass-=self.members[i].size
			self.members[i].size = 0
			self.population-=1
			return 1
		else:
			return 0
# retunrs the amout of food to add back into the system
# note that id 0 is grass
# note that id 1 is Meat on ground
# hunnting rule can be added here
	def can_eat(self,species_id):
		return species_id in self.can_eat_list

# simple list of id to kill returns the food to add to the system
	def Remove_killed_members(self,alist):
		alist.sort()
		for i in reversed(alist):
			del self.members[i]
		
# list of (x,y,size) locations to make a new member
	def add_members(self,alist):
		for i in alist:
			self.population += 1
			self.members.append(Creature(i[0],i[1],i[2]))
			self.population_mass+=self.kid_size;

#returns a list of x, y or kids if can not have a kid it is of size 0
	def havekid(self):
		alist = []
		for i in self.members:
			if i.size >= self.kid_size*2:
				alist.append((i.x,i.y,self.kid_size))
				i.size -= self.kid_size
				self.population_mass -= self.kid_size
		return alist


	def printmembers(self):
		for i in self.members:
			print(i.toString())

	def printmember(self,i):
		print(self.members[i].toString())