from ChildRules import *
class SingleChild (ChildRules):
	def __init__(self):
		a =1

	def havekid(self,creature,max_size,min_size,kid_size,kid_stomach_size,safty):
		alist = []
		if(creature.size>kid_size+kid_stomach_size+min_size+safty):
			creature.size = creature.size-kid_size-kid_stomach_size
			alist.append((creature.x,creature.y))
		return alist
