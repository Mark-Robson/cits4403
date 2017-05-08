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
from time import gmtime, strftime

alist = []
alist.append(0)
world_size = 250
starting_food = world_size*world_size*15
simelength = 50

dermps = SpeciesFactory.verysmallHerbfast(1000,world_size,1,alist)

file = open("testfile"+strftime("%Y_%m_%d_%H_%M_%S", gmtime())+".csv","w")

worldmap = SimpleSquare(RandomFoodSystem(world_size),world_size)
worldmap.addFood(starting_food)

print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food "+str(dermps.population))
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+" food\n")
faim = worldmap.getTotalFood()+dermps.totalMass();
o = 0 
for x in range(20):
	if(x == 0 or x == 3 or x == 7 or x == 11):
		faim = faim
	elif(x == 12):
		worldmap.addFood(faim)
		faim = int(faim*2)
	elif(x==15):
		faim = int(faim/4)
	elif( x%2 == 1 ):
		worldmap.addFood(faim)
		faim = int(faim*2)
	elif( x%2 == 0):
		faim = int(faim/2)
	else:
		faim = 0
	
	for i in range(simelength):
		cm = dermps.totalMass()
		wm = worldmap.getTotalFood()
		pop = dermps.population
		
		deadlist = []
		kidlist = []
		
		pop = dermps.population
		file.write(str(pop)+","+str(o)+","+str(cm)+","+str(wm)+","+str(wm+cm)+"\n")
		o = o + 1
		for c in range(pop):
			x,y = dermps.move(c,0)
			food_before = worldmap.getfood(x,y)
			(left_tile, back_later) = dermps.eat(c,food_before)
			worldmap.removefood(x,y,food_before-left_tile)
			isdead , h = dermps.hunger(c)
			 
			back_later = back_later + dermps.grow(c)
			back_later = back_later + h
			if (wm+cm <= faim):
				worldmap.addFood(int(back_later))

			if(isdead == 1):
				deadlist.append(c)
			else:
				kidlist = kidlist+dermps.havekid(c)
		killfood = dermps.Hunger_kill_members(deadlist)
		killmass = 0

		for K in killfood:
			killmass = killmass +K[2]
		dermps.add_members(kidlist)
		wm = worldmap.getTotalFood()
		cm = dermps.totalMass()
		
		# print (str(wm+cm)+" adding "+str(back_later)+"aiming "+str(faim))
		if (wm+cm <= faim):
			worldmap.addFood(int(faim-wm-cm))
		else:
			worldmap.addFood(int(killmass/2))


	print ("the world contains "+str(worldmap.getTotalFood())+"food")
	print ("the creature have  "+str(dermps.totalMass())+"food there are "+str(dermps.population))
	print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+" food\n")

