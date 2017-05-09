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
world_size = 25
starting_food = world_size*world_size*15
simelength = 10

dermps =  SpeciesFactory.verysmallHerbfast(1,world_size,1,alist)
alist = []
alist.append(1)
dermps2 = SpeciesFactory.verysmallHerbfast(1,world_size,2,alist)

file = open("testfile"+strftime("%Y_%m_%d_%H_%M_%S", gmtime())+".csv","w")

worldmap = SimpleSquare(RandomFoodSystem(world_size),world_size)
worldmap.addFood(starting_food)

print ("the world contains "+str(worldmap.getTotalFood())+"food")
print ("the creature have  "+str(dermps.totalMass())+"food "+str(dermps.population))
print ("the total food is  "+str(worldmap.getTotalFood()+dermps.totalMass())+" food\n")
faim = worldmap.getTotalFood()+dermps.totalMass()+dermps2.totalMass();
o = 0 
file.write("timestep,pray,pred,time,creatue biomass,map biomass,totalmass\n")
for masterloop in range(5):
	print(masterloop)
	for i in range(simelength):
		cm = dermps.totalMass()+dermps2.totalMass()
		wm = worldmap.getTotalFood()
		pop = dermps.population
		
		deadlist = []
		kidlist = []
		
		pop = dermps.population
		pop2 = dermps2.population

		file.write(str(o)+","+str(pop)+","+str(pop2)+","+str(o)+","+str(cm)+","+str(wm)+","+str(wm+cm)+"\n")
		o = o + 1
		for c in range(pop):

			print("i am "+str(c))

			dermps.printmember(c)
			x,y = dermps.move(c,0)
			food_before = worldmap.getfood(x,y)
			print("trying to eat "+str(food_before))
			(left_tile, back_later) = dermps.eat(c,food_before)
			dermps.printmember(c)
			print("i left"+str(left_tile))
			worldmap.removefood(x,y,food_before-left_tile)
			dermps.printmember(c)

			isdead,alist,h = dermps.hunger(c)

			print("i lost food "+str(h))

			dermps.printmember(c)
			
			back_later = back_later + dermps.grow(c)
			print("i grow ")
			dermps.printmember(c)
			back_later = back_later + h
			print("\n")
			if(isdead == 1):
				back_later = back_later + alist[0][2]
				deadlist.append(c)
				#print("i am dead now/cry")
			else:
				print("befor i have kids ")
				dermps.printmember(c)
				kidlist = kidlist+dermps.havekid(c)
				dermps.printmember(c)
			
			#print(str(back_later)+"food added back")
			#if (wm+cm+back_later <= faim):
			worldmap.addFood(int(back_later))
			#elif(wm+cm< faim):
			#	temp = faim - (wm+cm)
			#	worldmap.addFood(int(temp))

		dermps.Hunger_kill_members(deadlist)
		# out with the old
		dermps.add_members(kidlist)
		# in with the new
		if(masterloop>2):
			if(i == 0 ):
				print("ok")
			deadlist = []
			kidlist = []
			praysets = [[ [] for i in range(world_size)] for i in range(world_size)]
			pop = dermps.population
			cm = dermps.totalMass()+dermps2.totalMass()
			wm = worldmap.getTotalFood()

			for c in range(pop):
				x,y = dermps.getlocation(c)
				praysets [x][y].append(c)

			for c in range(pop2):

				x,y = dermps2.move(c,0)

				totalfood = int(0)
				praydeathlist = []
				for p in praysets[x][y]:
					temp = dermps.get_eaten(p)
					totalfood = totalfood + temp[0][2]
					praydeathlist.append(p)
				praysets[x][y] = []

				#dermps2.printmember(c)
				#print ( "pred eating " + str ( totalfood ))
				(left_tile, back_later) = dermps2.eat(c,totalfood)
				#dermps2.printmember(c)
				#print(str(back_later)+"                           "+str(left_tile))
				isdead,alist,h = dermps2.hunger(c)
				#dermps2.printmember(c)
				 
				back_later = back_later + dermps2.grow(c)
				back_later = back_later + h +left_tile
				#print("adding back"+str(back_later))

				if(isdead == 1):
					back_later = back_later + alist[0][2]
					deadlist.append(c)
				else:
					kidlist = kidlist+dermps2.havekid(c)
				#print("adding back"+str(back_later))
				
				#if (wm+cm+back_later <= faim):
				worldmap.addFood(int(back_later))
				#elif(wm+cm< faim):
				#	temp = faim - (wm+cm)
				#	worldmap.addFood(int(temp))

			dermps2.Hunger_kill_members(deadlist)
			dermps.Hunger_kill_members(praydeathlist)
			# out with the old
			dermps2.add_members(kidlist)
