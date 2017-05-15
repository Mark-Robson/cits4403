from Species import *
from WorldMap import *
import random
from time import gmtime, strftime
import argparse

parser = argparse.ArgumentParser(description='Creates the world sim in a\
prededator prey model.')
parser.add_argument('--startingpraypop', '-pray',
                    type=int,
                    help='Integer representing initial number of pray species.',
                    default=100)
parser.add_argument('--startingpredpop', '-pred',      
                    type=int,
                    help='Integer representing initial number of predator\
                    species',
                    default=100)      
parser.add_argument('--length', '-L',
                    type=int,
                    help='Integer value representing the number\
                    of time steps in the simulation',
                    default=1000)      
parser.add_argument('--world_size', '-S',
                    type=int,  
                    help='Integer value representing N, the length of one side \
                    of the world. Total world size = N*N',
                    default=200)      
parser.add_argument('--fileout', '-F',
                    type=int,
                    help='Integer value representing the number of instant \
                    between each file print statement',
                    default=1)       
parser.add_argument('--avefoodpertile', '-food',
                    type=int,
                    help='Integer value represnting the average amount of per \
                    tile',
                    default=5)           
args = parser.parse_args()        
world_size = args.world_size      
StartingPrayPop = args.startingpraypop        
StartingPredPop = args.startingpredpop        
length = args.length      
fileout = args.fileout        
avefood = args.avefoodpertile     
     
print(args)       
starting_food = world_size * world_size * avefood

alist = []
alist.append(0)

worldmap = SimpleSquare(world_size)
worldmap.addFood(starting_food)
#              map,species_id,can_eat_list,min_size,kid_size
pray = Species(worldmap, 1, alist, 10, 20)
startingPop = []
for i in range(StartingPrayPop):
    x = random.randint(0, world_size-1)
    y = random.randint(0, world_size-1)
    startingPop.append( (x, y, pray.getkid_size()) )
pray.add_members(startingPop)


alist = []
alist.append(1)

pred = Species(worldmap, 2, alist, 10, 20)
newstartingPop = []
for i in range(StartingPredPop):
    x = random.randint(0, world_size-1)
    y = random.randint(0, world_size-1)
    newstartingPop.append( (x, y, pred.getkid_size()) )
pred.add_members(newstartingPop)

time = 0
prayMass = pray.getPopulationMass()
perdMass = pred.getPopulationMass()
prayPopulation = pray.getPopulation()
predPopulation = pred.getPopulation()
worldmass = worldmap.getTotalFood()
totalmass = worldmass+prayMass+perdMass

massAim = totalmass

file = open("testfile"+strftime("%Y_%m_%d_%H_%M_%S", gmtime())+".csv", "w")

print (str(time)+"\nthe world contains "+str(worldmass)+"food\nthe pray     have  "+str(prayMass)+" food "+str(prayPopulation)+"\nthe pred     have  "+str(perdMass)+" food "+str(predPopulation)+"\nthe total food is  "+str(totalmass)+"food\n")
# print (str(pray.slowPopulationMass())+" "+str(len(pray.members)))

file.write(str(time)+","+str(prayPopulation)+","+str(predPopulation)+","+str(time)+","+str(prayMass)+","+str(perdMass)+","+str(worldmass)+","+str(totalmass)+"\n")

for i in range(length):

    pray.stepSpecies()

    prayMass = pray.getPopulationMass()
    perdMass = pred.getPopulationMass()
    prayPopulation = pray.getPopulation()
    predPopulation = pred.getPopulation()
    worldmass = worldmap.getTotalFood()
    totalmass = worldmass+prayMass+perdMass

    if(totalmass < massAim):
        worldmap.addFood(int(massAim-totalmass))
        worldmass = worldmap.getTotalFood()
        totalmass = worldmass+prayMass+perdMass

    if(time>50):
        pred.stepSpecies()

        prayMass = pray.getPopulationMass()
        perdMass = pred.getPopulationMass()
        prayPopulation = pray.getPopulation()
        predPopulation = pred.getPopulation()
        worldmass = worldmap.getTotalFood()
        totalmass = worldmass+prayMass+perdMass

        if(totalmass < massAim):
            worldmap.addFood(int(massAim-totalmass))
            worldmass = worldmap.getTotalFood()
            totalmass = worldmass+prayMass+perdMass

    time += 1
    if(time%fileout==0):
        file.write(str(time)+","+str(prayPopulation)+","+str(predPopulation)+","+str(time)+","+str(prayMass)+","+str(perdMass)+","+str(worldmass)+","+str(totalmass)+"\n")

    print (str(time)+"\nthe world contains "+str(worldmass)+"food\nthe pray     have  "+str(prayMass)+" food "+str(prayPopulation)+"\nthe pred     have  "+str(perdMass)+" food "+str(predPopulation)+"\nthe total food is  "+str(totalmass)+"food\n")
