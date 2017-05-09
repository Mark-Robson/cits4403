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
world_size = 200
starting_food = world_size*world_size*10
dermps = SpeciesFactory.simplesmallHerbfast(10,world_size,1,alist)

file = open("testfile"+strftime("%Y_%m_%d_%H_%M_%S", gmtime())+".csv","w")

worldmap = SimpleSquare(RandomFoodSystem(world_size),world_size)
worldmap.addFood(starting_food)

print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food "+str(dermps.population))
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+" food\n")

for i in range(5000):
	# worldmap.print_map()
	cm = dermps.totalMass()
	wm = worldmap.getTotalFood()
	pop = dermps.population
	print(str(pop)+","+str(i)+","+str(cm)+","+str(wm)+"\n");
	deadlist = []
	kidlist = []
	
	file.write(str(pop)+","+str(i)+","+str(cm)+","+str(wm)+"\n")
	
	# dermps.printmembers()
	for c in range(pop):

		# print ("i am "+str(c)+" at size "+str(dermps.getfoodsize(c)))
		x,y = dermps.move(c,0)
		# print(str(x)+" "+str(y))
		food_before = worldmap.getfood(x,y)
		# print("i eat try "+str(food_before))
		# print (str(dermps.getfoodsize(c))+"befor eating")
		(left_tile, back_later) = dermps.eat(c,food_before)
		# print (str(dermps.getfoodsize(c))+"after eating")



		# print ("the world contains "+str(worldmap.getTotalFood())+"food")
		worldmap.removefood(x,y,food_before-left_tile)
		# print ("the world contains "+str(worldmap.getTotalFood())+"food")

		# print("i leave "+str(worldmap.getfood(x,y)))


		# print (str(dermps.getfoodsize(c))+"befor hunger")
		isdead , h = dermps.hunger(c)
		# print (str(dermps.getfoodsize(c))+"after hunger")

		# print (str(dermps.getfoodsize(c))+"befor grow")
		back_later = back_later + dermps.grow(c)
		# print (str(dermps.getfoodsize(c))+"after grow")

		back_later = back_later + h
		if(isdead == 1):
			deadlist.append(c)
			# print("i am dead >.<"+str(dermps.getfoodsize(c)))
		else:
			
			# print (str(dermps.getfoodsize(c))+"befor trying to have kids")
			kidlist = kidlist+dermps.havekid(c)
			# print (str(dermps.getfoodsize(c))+"after trying to have kids")

		# print ("i am "+str(c)+" at size "+str(dermps.getfoodsize(c)))
		# print ("adding some fod back "+str(back_later)+"\n")
		
		worldmap.addFood(back_later)


	killfood = dermps.Hunger_kill_members(deadlist)
	for K in killfood:
		# print("addding back "+str(K[2]))
		worldmap.addFood(K[2])


	dermps.add_members(kidlist)


print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food there are "+str(dermps.population))
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+" food\n")
