from creature import *
from herbivore import *
from world import *
from randomworld import *
from simulation import *
import numpy
import random


simulations = simulation.newrandomworld()
simulations.printsim()
for i in range(1):
	# simulations.printsim()
	simulations.stepsim()
	# print(len(simulations.creatures))

simulations.printsim()