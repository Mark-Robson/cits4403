
class Creature:
	
	def __init__(self,in_x,in_y,in_kid_size):
		self.x = in_x
		self.y = in_y
		self.size = in_kid_size

	def getMass(self):
		return int(self.size + self.stomach)

	def getfoodmass(self):
		return (self.size , self.stomach)

	def toString(self):
		return str((self.x,self.y,self.size))

