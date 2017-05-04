from FoodSystem import *

class WorldMap:
	__food_system
	__total_food
	__mapsize


	def __init__(self , FoodSystem , size)
	self.__food_system = FoodSystem
	self.__total_food = 0
	self.__mapsize = size

# asks the food system where to add the amount of food to the system
# addes the food to that set of tiles
	def addFood(self , amount):
		self.__food_system.addFood(amount)
		self.__total_food = self.__total_food + amount

	def getTotalFood(self):
		return __total_food
# This will retunr the amount of food on tile at x,y
	def getfood(self , x , y):
		return self.__total_food

# This will try to remove amount food for tile at x, y returning the amount of 
# food that was removed 
	def removefood(self , x , y , amount):
		if(amount>self.__total_food):
			amount = self.__total_food
			return amount
		self.__total_food = self.__total_food - amount
		return amount

	def getSize(self):
		return self.mapsize
		