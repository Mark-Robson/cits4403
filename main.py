from creature import *
from herbivore import *
from world import *
from randomworld import *
from simulation import *
import numpy
import random


simulations = simulation.newrandomworld(100,100,100000)
# simulations.printsim()
file = open("testfile.csv","w") 
totalfoodstart = simulations.creaturefood()+simulations.simworld.totalfood

print ("the world contains "+str(simulations.simworld.totalfood)+"food")
print ("the creature have  "+str(simulations.creaturefood())+"food")
print ("the total food is  "+str(simulations.creaturefood()+simulations.simworld.totalfood)+"food")
for i in range(1000):
	# simulations.printsim()
	print(i)
	file.write(simulations.stepsim()+"\n")
	# print(len(simulations.creatures))

simulations.simworld.addamountfood(int(10),100000)
simulations.maxfood = simulations.maxfood +100000
for i in range(1000):
	# simulations.printsim()
	print(i)
	file.write(simulations.stepsim()+"\n")
	# print(len(simulations.creatures))
simulations.maxfood = simulations.maxfood -150000
for i in range(1000):
	# simulations.printsim()
	print(i)
	file.write(simulations.stepsim()+"\n")
	# print(len(simulations.creatures))



file.close() 
print ("the world contains "+str(simulations.simworld.totalfood)+"food")
print ("the creature have  "+str(simulations.creaturefood())+"food")
print ("the total food is  "+str(simulations.creaturefood()+simulations.simworld.totalfood)+"food")
# simulations.printsim()