class DeathRules:

	def __init__(self):
		a = 0

# simple list of id to kill returns the food to add to the system
#  at a list of (x,y,amount)
#  for x or y = -1 add randomly 
# TODO MAKE THIS MEAT NOT GRASS
	def hunger(self,creature):
		alist = []
		alist.append((-1,-1,creature.getMass()))
		return alist

# simple list of id to kill returns the food to add to the system
#  at a list of (x,y,amount)
#  for x or y = -1 add randomly 
#  for x or y = -2 add to the eater 
# TODO MAKE THIS MEAT NOT GRASS
	def eaten(self,creature):
		alist = []
		alist.append((-1,-1,creature.stomach))
		return (-2,-2,creature.size)