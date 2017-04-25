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
		simworld.addfood(10000)

		return simulation(simworld,creatures)


	def printsim (self):

		printer =  numpy.zeros((self.simworld.getSize(),self.simworld.getSize()))
		for i in self.creatures:
			printer[i.getX_co][i.getY_co] = 'D'
			i.printcre()

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				if(printer[i][j]!='D'):
					printer[i][j] = self.simworld.getfood(i,j)

		for i in range(self.simworld.getSize()):
			for j in range(self.simworld.getSize()):
				
				sys.stdout.write(('%5s ' % (str(printer[i][j])) ))
			sys.stdout.write('\n')


		sys.stdout.flush()




