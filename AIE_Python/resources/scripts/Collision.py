import math

# A* class

class CCollision:
	def __init__(self, entity, radius):
		self.Position = entity.Position
		self.Radius = radius
		
	def update(self, entity):
		self.Position = entity.Position
	
	@staticmethod
	def CircleCollision(firstCircle, secondCircle):
		#Calculate Differences Between Centers
		distX = (float(firstCircle.Position.x) - float(secondCircle.Position.x))
		distY = (float(firstCircle.Position.y) - float(secondCircle.Position.y))

		distS = (float((distX * distX))) + (float((distY * distY)))

		if (float(distS)) <= (float((firstCircle.Radius + secondCircle.Radius) ** 2)):
			return True
		else:
			return False
			