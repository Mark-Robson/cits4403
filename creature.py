class creature:
	food = 0
	x_co = 0
	y_co = 0
	speed = 0
	species_id = 0
	childSize = 0
	healthySize = 0

	def __init__(self,foodlevel,xco,yco,newspeed,species_id,childSize,healthySize):
		self.food = foodlevel
		self.x_co = xco
		self.y_co = yco
		self.speed = newspeed
		self.species_id = species_id
		self.healthySize = healthySize
		self.childSize = childSize

	def getSpecies_id(self):
		return self.species_id

	def getFood(self):
		return self.food

	def getX_co(self):
		return self.x_co

	def getY_co(self):
		return self.y_co

	def getSpeed(self):
		return self.speed

	def getChildSize(self):
		return self.childSize

	def gethealthySize(self):
		return self.healthySize

	def setSpecies_id (self,species_id):
		self.species_id = species_id

	def setFood(self,newfood):
		self.food = newfood

	def setX_co(self,newx_co):
		self.x_co = newx_co

	def setY_co(self,newy_co):
		self.y_co = newy_co
	
	def setSpeed(self,newspeed):
		self.speed = speed

	def setSpeed(self,newspeed):
		self.speed = speed

	def addFood(amount):
		self.food += amount

	def nextmove(self):
		return x_co,y_co

	def caneat(self,foodid):
		if(foodid==(-1)):
			return true
		else:
			return false

	def printcre(self):
		print("Food ="+str(self.food)+
		"x ="+str(self.x_co )+
		"y ="+str(self.y_co )+
		"speed ="+str(self.speed )+
		"species_id ="+str(self.species_id)+
		"healthySize ="+str(self.healthySize)+
		"childSize ="+str(self.childSize))
