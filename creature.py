
class Creature:
	x =int(0)
	y =int(0)
	size =int(0)

	def __init__(self,x,y,kid_size):
		self.x = x
		self.y = y
		self.size = kid_size

	def getMass(self):
		return int(self.size + self.stomach)

	def getfoodmass(self):
		return (self.size , self.stomach)

	def toString(self):
		return str((self.x,self.y,self.size))

