from creature import *
from herbivore import *
from world import *
from randomworld import *
from simulation import *

import sys

class simulation:

	simworld = world(1);
	creatures = []

	def __init__(self,simworld,creature):
		self.simworld = simworld
		self.creature = creature


	def newrandomworld():
		# (self,foodlevel,xco,yco,newspeed,species_id,childSize,healthySize,worldsize)
		creatures = []
		creatures.append(herbivore(50,0,0,1,0,20,50,10))
		creatures.append(herbivore(50,0,5,1,0,20,50,10))
		creatures.append(herbivore(50,5,0,1,0,20,50,10))
		creatures.append(herbivore(50,5,3,1,0,20,50,10))
		creatures.append(herbivore(50,3,5,1,0,20,50,10))
		creatures.append(herbivore(50,3,3,1,0,20,50,10))
		simworld = randomworld(10)
		simworld.addfood(1000)
		return simulation(simworld,creatures)

	def printsim (self):
		length = len(self.creature)
		printer =  [[ "" for i in range(self.simworld.getSize())] for j in range(self.simworld.getSize())] 
		for i in range(length):
			printer[int(self.creature[i].y_co)][int(self.creature[i].x_co)] = "deer"
			self.creature[i].printcre()

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				if(printer[i][j]!="deer"):
					printer[i][j] = self.simworld.getfood(i,j)

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				
				sys.stdout.write(('%5s ' % (str(printer[i][j])) ))
			sys.stdout.write('\n')


		sys.stdout.flush()

	def stepsim(self):
		newfood = int(0)
		births = int(0)
		deaths = int(0)
		for i in self.creature[:]:
			# i.printcre()
			newfood = newfood + i.nextmove();

			foodtoadd = self.simworld.removefood(int(i.x_co),int(i.y_co))
			newfood = newfood + foodtoadd
			i.food = i.food + foodtoadd
			currentfood = i.getFood()
			# print(currentfood)
			if(currentfood < 0):
				print ("a critter is dead !!"+str(len(self.creature)))
				deaths = deaths + 1
				del i
				print ("!!"+str(len(self.creature)))
			elif(currentfood > (i.healthySize+i.childSize)):
				births = births+1
				print("was of size "+str(i.food ))
				self.creature.append(herbivore(i.childSize,i.x_co,i.y_co,i.speed,i.species_id,i.childSize,i.healthySize,i.worldsize))
				i.food = i.food - i.childSize
				# print("now of size "+str(i.food ))
		# print ("adding food in the amount of "+str(newfood))
		self.simworld.addfood(int(newfood))
		print(str(len(self.creature))+","+str(births)+","+str(deaths))

										
			
