# from sets import *
from WorldMap import *
import random


class Species:

    specieslist = []
    speciesidlist = []

    def __init__(self, in_map, in_species_id, in_can_eat_list, in_min_size, in_kid_size):
        self.specieslist.append(self)
        self.speciesidlist.append(in_species_id)
        self.worldmap = in_map
        self.species_id = in_species_id
        self.can_eat_list = set(in_can_eat_list)
        self.min_size = in_min_size
        self.kid_size = in_kid_size
        self.world_size = self.worldmap.mapsize
        self.population_mass = 0
        self.membersx = []
        self.membersy = []
        self.members_size = []

    def getkid_size(self):
        return self.kid_size

    def getPopulation(self):
        return len(self.membersx)

    def getPopulationMass(self):
        return self.population_mass

    def slowPopulationMass(self):
        count = 0
        for i in self.members_size:
            count+= i
        return count

    def getlocation(self, i):
        return self.membersx[i], self.membersy[i]

    def stepSpecies(self):

        praymap = []
        for x in range(self.world_size):
            praymap.append([])
            for y in range(self.world_size):
                praymap[x].append([])

        prayKilledList = []
        for s in range(len(self.speciesidlist)):
            prayKilledList.append([])
            if self.speciesidlist[s] in self.can_eat_list:

                for specimen in range(len(self.specieslist[s].membersx)):
                    cs = self.specieslist[s].members_size[specimen]
                    cx = self.specieslist[s].membersx[specimen]
                    cy = self.specieslist[s].membersy[specimen]
                    praymap[cx][cy].append((s,specimen,cs))


        # Creatures that will be killed at end of sim
        alist = []
        # For every creature
        for i in range(len(self.membersx)):
            # Move a creature
            # If it lands on food it'll eat. Yum Yum. Eating is part of moving.
            self.move(i, 1, praymap, prayKilledList)
            # This is dying due to hunger
            if(self.hunger(i, 1)):
                alist.append(i)
        # Clean steps. Remove all creatures
        self.Remove_killed_members(alist)

        for prayType in range(len(self.speciesidlist)):
            self.specieslist[prayType].Remove_consumed_members(prayKilledList[prayType])
        # New pop creation
        newPop = []
        # Checks for children
        newPop = self.havekid()
        self.add_members(newPop)

    def move(self, i, speed , praymap ,prayKilledList):
        # Calculate max and min x for movement
        minx = self.membersx[i]-speed
        maxx = self.membersx[i]+speed
        if(self.membersx[i]-speed < 0):
            minx = 0
        if(self.membersx[i]+speed > self.world_size-1):
            maxx = self.world_size-1

        # Calculate max and min y for movement
        miny = self.membersy[i]-speed
        maxy = self.membersy[i]+speed
        if(self.membersy[i]-speed < 0):
            miny = 0
        if(self.membersy[i]+speed > self.world_size-1):
            maxy = self.world_size-1

        # Actually generate the random numbers
        self.membersx[i] = random.randint(minx, maxx)
        self.membersy[i] = random.randint(miny, maxy)

        # This is specifically intended for eating grass
        if(0 in self.can_eat_list):
            self.eatgrass(i)

        # TODO: Eat other things
        amount = 0
        for p in praymap[self.membersx[i]][self.membersy[i]]:
            prayKilledList[p[0]].append(p[1])
            amount+= p[2]
        praymap[self.membersx[i]][self.membersy[i]] = []

        # This increments the size the specimen
        self.members_size[i] += amount
        # We keep count of total mass in each species type
        self.population_mass += amount


    def eatgrass(self, i):
        # find out food on tile
        amount = self.worldmap.getfood(self.membersx[i], self.membersy[i])
        # This removes the food fromthe map
        self.worldmap.removefood(self.membersx[i], self.membersy[i], amount)
        # This increments the size the specimen
        self.members_size[i] += amount
        # We keep count of total mass in each species type
        self.population_mass += amount

    # Returns 1 if dead from hunger 0 if not
    def hunger(self, i, amount):
        # Things can hunger at variable rates, default should be 1. This is
        # the 'amount' variable.
        self.members_size[i] -= amount
        self.population_mass -= amount

        # This is actually figuring out if they're dead
        if(self.members_size[i] < self.min_size):
            self.population_mass -= self.members_size[i]
            self.members_size[i] = 0
            return 1
        else:
            return 0

    # This checks if specimen can eat specimen
    def can_eat(self, sid):
        return sid in self.can_eat_list

    # Simple list of id to kill
    # Literally deletes the memory from the species list
    def Remove_killed_members(self, alist):
        alist.sort()
        for i in reversed(alist):
            del self.membersx[i]
            del self.membersy[i]
            del self.members_size[i]

    def Remove_consumed_members(self, alist):
        alist.sort()
        for i in reversed(alist):
            self.population_mass-= self.members_size[i]
            self.members_size[i] = 0
            del self.membersx[i]
            del self.membersy[i]
            del self.members_size[i]

    # List of (x,y,size) locations to make a new member
    # This is called in births and in startup
    # Alist is a list of tuples x loc, y loc and size.
    def add_members(self, alist):
        for i in alist:
            self.membersx.append(i[0])
            self.membersy.append(i[1])
            self.members_size.append(i[2])
            self.population_mass += self.kid_size

    # Returns a list of x, y and size if can not have a kid it is empty []
    # Checks if can have a kid
    def havekid(self):
        alist = []
        for i in range(len(self.membersx)):
            if(( self.members_size[i]) >= (self.kid_size*2)):
                kidsize = self.kid_size
                alist.append((self.membersx[i],self.membersy[i],kidsize))
                self.population_mass -= kidsize
                self.members_size[i] -= kidsize
        return alist
