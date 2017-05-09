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
world_size = 10
starting_food = 2000000
dermps = SpeciesFactory.simpleLargeHerb(10,world_size,1,alist)

file = open("testfile.csv","w")

worldmap = SimpleSquare(RandomFoodSystem(world_size),world_size)
worldmap.addFood(starting_food)

print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food"+str(dermps.population))
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+"food\n")



for i in range(3):
	worldmap.print_map()
	deadlist = []
	kidlist = []
	for c in range(dermps.population):

		x,y = dermps.move(c,0)
		# print(str(x)+" "+str(y))
		food_before = worldmap.getfood(x,y)
		(left_tile, back_later) = dermps.eat(c,food_before)
		# print("aaaaaa "+str(food_before))
		worldmap.removefood(x,y,food_before-left_tile)
		isdead = dermps.hunger(c)

		if(isdead == 1):
			deadlist.append(c)
		else:
			back_later = back_later + dermps.grow(c)
			kidlist = kidlist+dermps.havekid(c)

		# print (back_later)
		worldmap.addFood(back_later)

	killfood = dermps.Hunger_kill_members(deadlist)
	for i in killfood:
		worldmap.addFood(i[2])


	dermps.add_members(kidlist)


	print ("the world contains "+str(worldmap.getTotalFood())+"food")
	print ("the creature have  "+str(dermps.totalMass())+"food there are "+str(dermps.population))
	print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+"food\n")

