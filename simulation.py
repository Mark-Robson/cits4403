from creature import *
from herbivore import *
from world import *
from randomworld import *
from simulation import *

import sys

class simulation:

	simworld = world(1)
	creatures = []
	maxfood = 0 


	def __init__(self,simworld,creature):
		self.simworld = simworld
		self.creature = creature


	def newrandomworld(numderps,mapsize,startsize):
		# (self,foodlevel,xco,yco,newspeed,species_id,childSize,healthySize,worldsize)
		creatures = []

		for i in range (numderps):
			x = random.randint(0,mapsize-1);
			y = random.randint(0,mapsize-1);
			creatures.append(herbivore(10,x,y,1,0,10,20,mapsize))
		simworld = randomworld(mapsize)
		simworld.addamountfood(int(startsize/100),startsize)
		a = simulation(simworld,creatures)
		a.maxfood = startsize
		return a

	def printsim (self):
		length = len(self.creature)
		cfood = 0 
		printer =  [[ "" for i in range(self.simworld.getSize())] for j in range(self.simworld.getSize())] 
		for i in range(length):
			printer[int(self.creature[i].y_co)][int(self.creature[i].x_co)] = "deer"
			self.creature[i].printcre()
			cfood = cfood + self.creature[i].food

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				if(printer[i][j]!="deer"):
					printer[i][j] = self.simworld.getfood(i,j)

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				
				sys.stdout.write(('%5s ' % (str(printer[i][j])) ))
			sys.stdout.write('\n')

		print ("the world contains "+str(self.simworld.totalfood)+"food")
		print ("the cretures have  "+str(cfood)+"food")
		sys.stdout.flush()

	def creaturefood(self):
		cfood = 0
		for i in range(len(self.creature)):
			cfood = cfood + self.creature[i].food
		return cfood
								
	def stepsim(self):
		leng = len(self.creature)
		newfood = int(0)
		births = int(0)
		deaths = int(0)
		deathlist = []
		deathlist.append(int(-1))
		babylist = []
		for i in range(leng):
			# i.printcre()
			newfood = newfood + self.creature[i].nextmove();

			foodtoadd = self.simworld.removefood(int(self.creature[i].x_co),int(self.creature[i].y_co))
			# print(foodtoadd)
			# newfood = newfood + foodtoadd
			self.creature[i].food = self.creature[i].food + foodtoadd
			currentfood = self.creature[i].getFood()
			# print(currentfood)
			if(currentfood <= 0):
				# print ("a critter is dead !!"+str(len(self.creature)))
				deaths = deaths + 1
				deathlist.append(i)
				# print ("!!"+str(len(self.creature)))
			elif(currentfood > (self.creature[i].healthySize+self.creature[i].childSize)):
				births = births+1
				# print("was of size "+str(self.creature[i].food ))
				babylist.append(herbivore(self.creature[i].childSize,self.creature[i].x_co,self.creature[i].y_co,self.creature[i].speed,self.creature[i].species_id,self.creature[i].childSize,self.creature[i].healthySize,self.creature[i].worldsize))
				self.creature[i].food = self.creature[i].food - self.creature[i].childSize
				# print("now of size "+str(self.creature[i].food ))
		# print ("adding food in the amount of "+str(newfood))
		
		# print (str(self.maxfood) +"     "+str(self.creaturefood())+"     "+str(self.simworld.totalfood))
		if(self.maxfood>=newfood+self.creaturefood()+self.simworld.totalfood):
			# print ("feed the derps"+str(newfood))
			self.simworld.addfood(int(newfood))
		elif (self.maxfood > self.creaturefood()+self.simworld.totalfood):
			# print ("feed the derps"+str(self.maxfood-self.creaturefood()-self.simworld.totalfood))
			self.simworld.addfood(int(self.maxfood-self.creaturefood()-self.simworld.totalfood))
		#TODO Hiss de shush
		# print(str(len(deathlist)))
		if(deaths>0):
			for i in reversed(deathlist):
				if(i>=0):
					del self.creature[i]
		for i in babylist:
			self.creature.append(i)

		return (str(len(self.creature))+","+str(births)+","+str(deaths))







