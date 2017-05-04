
class FoodRules:
	def __init__(self):

#returns (the amount of food to be left on the tile ,
 # the amount of food to be added back into the system later ) 
	def eat (self,creature,food_in_tile,max_size,max_stomach_size,speed):
		return (food_in_tile,0)

#returns (1 if dead from hunger 0 if not , amount of food to add back to system )
	def hunger(self,creature,min_size,speed):
		return (0,0)

# returns the amount of food used to grow
	def grow(self,creature,grow_rate,max_size):
		return 0 
