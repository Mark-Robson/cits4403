from ChildRules import *
class SingleChild (ChildRules):
	def __init__(self):
		a =1

	def havekid(self,creature,max_size,min_size,kid_size,kid_stomach_size,safty):
		alist = []
		if(creature.size>kid_size+kid_stomach_size+min_size+safty):
			# print(str(creature.getfoodmass())+"befor removeing "+str((kid_size+kid_stomach_size)))
			creature.size = creature.size-(kid_size+kid_stomach_size)
			# print(str(creature.getfoodmass())+"after kid")
			alist.append((creature.x,creature.y))
		# else:
			# print("i am too small")
		return alist
