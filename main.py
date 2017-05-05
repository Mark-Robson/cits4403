from Species import *
from RandomMovement import *
from DeathRules import *
from CleanEater import *
from SingleChild import *
from SpeciesFactory import *
from WorldMap import *
from SpeciesFactory import *
from SpeciesFactory import *
from SimpleSquare import *
from RandomFoodSystem import *

alist = []
alist.append(0)
world_size = 1000
starting_food = 2000000
dermps = SpeciesFactory.simpleLargeHerb(10,world_size,1,alist)

file = open("testfile.csv","w")

worldmap = SimpleSquare(self, RandomFoodSystem(self,world_size,world_size))
worldmap.addFood(starting_food)

print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food")
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+"food")

for i in range(10):
	i = i+10


