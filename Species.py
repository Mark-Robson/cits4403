# from sets import *
from Creature import *
from WorldMap import *
import random


class Species:
    species_id = 0

    population = 0
    population_mass = 0
    min_size = 0
    kid_size = 0

    members = []
    can_eat_list = []

    world_size = int(0)
    map = WorldMap(1)

    def __init__(self, map, species_id, can_eat_list, min_size, kid_size):
        self.map = map
        self.species_id = species_id
        self.can_eat_list = set(can_eat_list)
        self.min_size = min_size
        self.kid_size = kid_size
        self.world_size = map.mapsize

    def getPopulationMass(self):
        return self.population_mass

    def getlocation(self, i):
        return self.members[i].x, self.members[i].y

    def stepSpecies(self):
        # Creatures that will be killed at end of sim
        alist = []
        # For every creature
        for i in range(self.population):
            # Move a creature
            # If it lands on food it'll eat. Yum Yum. Eating is part of moving.
            self.move(i, 10)
            # This is dying due to hunger
            if(self.hunger(i, 1)):
                alist.append(i)
        # Clean steps. Remove all creatures
        self.Remove_killed_members(alist)
        # New pop creation
        newPop = []
        # Checks for children
        newPop = self.havekid()
        self.add_members(newPop)

    def move(self, i, speed):
        # Calculate max and min x for movement
        minx = self.members[i].x-speed
        maxx = self.members[i].x+speed
        if(self.members[i].x-speed < 0):
            minx = 0
        if(self.members[i].x+speed > self.world_size-1):
            maxx = self.world_size-1

        # Calculate max and min y for movement
        miny = self.members[i].y-speed
        maxy = self.members[i].y+speed
        if(self.members[i].y-speed < 0):
            miny = 0
        if(self.members[i].y+speed > self.world_size-1):
            maxy = self.world_size-1

        # Actually generate the random numbers
        self.members[i].x = random.randint(minx, maxx)
        self.members[i].y = random.randint(miny, maxy)

        # This is specifically intended for eating grass
        if(0 in self.can_eat_list):
            self.eatgrass(i)

        # TODO: Eat other things

    def eatgrass(self, i):
        # find out food on tile
        amount = self.map.getfood(self.members[i].x, self.members[i].y)
        # This removes the food fromthe map
        self.map.removefood(self.members[i].x, self.members[i].y, amount)
        # This increments the size the specimen
        self.members[i].size += amount
        # We keep count of total mass in each species type
        self.population_mass += amount

    # Returns 1 if dead from hunger 0 if not
    def hunger(self, i, amount):
        # Things can hunger at variable rates, default should be 1. This is
        # the 'amount' variable.
        self.members[i].size -= amount
        self.population_mass -= amount

        # This is actually figuring out if they're dead
        if(self.members[i].size < self.min_size):
            self.population_mass -= self.members[i].size
            self.members[i].size = 0
            self.population -= 1
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
            del self.members[i]

    # List of (x,y,size) locations to make a new member
    # This is called in births and in startup
    # Alist is a list of tuples x loc, y loc and size.
    def add_members(self, alist):
        for i in alist:
            self.population += 1
            self.members.append(Creature(i[0], i[1], i[2]))
            self.population_mass += self.kid_size

    # Returns a list of x, y and size if can not have a kid it is empty []
    # Checks if can have a kid
    def havekid(self):
        alist = []
        for i in self.members:
            if i.size >= self.kid_size*2:
                alist.append((i.x, i.y, self.kid_size))
                i.size -= self.kid_size
                self.population_mass -= self.kid_size
        return alist

    # Don't use this one but it prints all things. Not grass.
    def printmembers(self):
        for i in self.members:
            print(i.toString())

    # This is the same but prints a single member.
    def printmember(self, i):
        print(self.members[i].toString())
