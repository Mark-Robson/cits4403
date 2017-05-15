from Species import *
from WorldMap import *
import random
from time import gmtime, strftime

# This is all map sim variables
world_size = 300
StartingPrayPop = 100
length = 1000
fileout = 10
starting_food = world_size*world_size*5

# Gen food map
worldmap = SimpleSquare(world_size)
worldmap.addFood(starting_food)

# map,species_id,can_eat_list,min_size,kid_size
# This is setting a species variables
alist = []
alist.append(0)
pray = Species(worldmap, 1, alist, 5, 10)

# Generate the species at random points in the world
startingPop = []
for i in range(StartingPrayPop):
    x = random.randint(0, world_size-1)
    y = random.randint(0, world_size-1)
    startingPop.append((x, y, pray.kid_size))
pray.add_members(startingPop)


time = 0
prayMass = pray.getPopulationMass()
prayPopulation = pray.population
worldmass = worldmap.getTotalFood()
totalmass = worldmass+prayMass


massAim = totalmass

file = open("testfile"+strftime("%Y_%m_%d_%H_%M_%S", gmtime())+".csv", "w")

print(str(time)+"\nthe world contains " + str(worldmass) + "food\nthe creature have  " + str(prayMass)+"food"+str(prayPopulation) + "\nthe total food is  "+str(totalmass)+"food\n")


file.write(str(time)+","+str(prayPopulation)+","+str(time)+","+str(prayMass)+","+str(worldmass)+","+str(totalmass)+"\n")

# This is the sim. Do not touch AT ALL.
for i in range(length):
    pray.stepSpecies()
    time += 1
    prayMass = pray.getPopulationMass()
    prayPopulation = pray.population
    worldmass = worldmap.getTotalFood()
    totalmass = worldmass+prayMass

    if(totalmass < massAim):
        worldmap.addFood(int(massAim-totalmass))
        worldmass = worldmap.getTotalFood()
        totalmass = worldmass+prayMass

    if(time % fileout == 0):
        file.write(str(time)+","+str(prayPopulation)+","+str(time)+","+str(prayMass)+","+str(worldmass)+","+str(totalmass)+"\n")

    print(str(time)+"\nthe world contains "+str(worldmass)+"food\nthe creature have  "+str(prayMass)+"food"+str(prayPopulation)+"\nthe total food is  "+str(totalmass)+"food\n")
