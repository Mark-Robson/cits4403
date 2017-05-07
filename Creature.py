
class Creature:
	x =0
	y =0
	size =0
	stomach =0

	def __init__(self,x,y,kid_size,kid_stomach_size):
		self.x = x
		self.y = y
		self.size = kid_size
		self.stomach = kid_stomach_size

	def getMass(self):
		return self.size + self.stomach


