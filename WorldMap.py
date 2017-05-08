from FoodSystem import *

class WorldMap:
	food_system = Foodsystem()
	total_food = int(0)
	mapsize = int(0)


	def __init__(self , FoodSystem , size):
		self.food_system = FoodSystem
		self.total_food = 0
		self.mapsize = size

# asks the food system where to add the amount of food to the system
# addes the food to that set of tiles
	def addFood(self , amount):
		self.food_system.addFood(amount)
		self.total_food = self.total_food + amount

	def getTotalFood(self):
		return self.total_food
# This will retunr the amount of food on tile at x,y
	def getfood(self , x , y):
		return self.total_food

# This will try to remove amount food for tile at x, y returning the amount of 
# food that was removed 
	def removefood(self , x , y , amount):
		if(amount>self.total_food):
			amount = self.total_food
			return amount
		self.total_food = self.total_food - amount
		return amount

	def getSize(self):
		return self.mapsize
