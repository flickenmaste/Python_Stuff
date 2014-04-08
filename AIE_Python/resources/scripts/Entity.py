import AIE
import game
import astar
from Collision import CCollision

#Tank Entity
#   A simple entity that can be placed on the screen with a right click, you should modify this so that the tank can be told to 
#   navigate to a point instead of instantly move.

class TankEntity:

	def __init__(self):
		self.Position = ( 1200, 600 )
		self.Rotation = 0
		self.spriteName = "./images/PlayerTanks.png"
		self.size = (57, 72 )
		self.origin = (0.5, 0.5)
		self.NodeList = []
		self.NodePos = []
		self.NodeIt = 0
		self.Collision = CCollision(self, self.size[0])
		self.spriteID = AIE.CreateSprite( self.spriteName, self.size[0], self.size[1], self.origin[0], self.origin[1], 71.0/459.0, 1.0 - 72.0/158.0, 128/459.0, 1.0 , 0xff, 0xff, 0xff, 0xff )
		print "spriteID", self.spriteID
		#Move Tile to appropriate location
		
		self.turret = Turret(self)
		
	def update(self, fDeltaTime ):
		mouseX, mouseY = AIE.GetMouseLocation()
		if( AIE.GetMouseButton(1)  ):
			self.Position = self.Seek(mouseX, mouseY)
		if( AIE.GetMouseButton(2) and (self.buttonPressed is False) ):
			self.buttonPressed = True
			self.BuildNode(mouseX, mouseY)
			if(self.NodeList[self.NodeIt] == True):
				self.VisitNode(self.NodePos[self.NodeIt])
				self.NodeIt += 1
		self.buttonPressed = not AIE.GetMouseButtonRelease(2)	
		AIE.MoveSprite( self.spriteID, self.Position[0], self.Position[1] )
		self.turret.update(fDeltaTime)
		self.Collision.update(self)
	
	def draw(self):
		
		AIE.DrawSprite( self.spriteID )
		self.turret.draw()
		
	def getImageName(self):
		return self.imageName
		
	def getState(self):
		return self.state
	
	def getSpriteID(self):
		return self.spriteID
		
	def setSpriteID(self, a_spriteID):
		self.spriteID = a_spriteID
	
	def getPosition(self):
		return self.Position

	def cleanUp(self):
		self.turret.cleanUp()
		AIE.DestroySprite( self.spriteID )
	
	# Custom functions
	
	# Basic seek function
	def Seek(self, mouseX, mouseY):
		lerpX = (self.Position[0] + (mouseX - self.Position[0]) * 0.1)
		lerpY = (self.Position[1] + (mouseY - self.Position[1]) * 0.1)
		Lerp = (lerpX, lerpY)
		return Lerp
		
	# Seek node
	def SeekNode(self, v2Pos):
		lerpX = (self.Position[0] + (v2Pos[0] - self.Position[0]) * 0.1)
		lerpY = (self.Position[1] + (v2Pos[1] - self.Position[1]) * 0.1)
		Lerp = (lerpX, lerpY)
		return Lerp

	# Basic node system
	def BuildNode(self, mouseX, mouseY):
		self.NodeList.append(True)
		self.NodePos.append((mouseX, mouseY))
		print self.NodeList
		
	# Visit basic node system
	def VisitNode(self, v2Pos):
		self.Position = self.SeekNode(v2Pos)
		return None
		
	# Avoid walls
	# def AvoidWall(self):
		
	
#Turret
#    This is an Entity Object that has an owner, it is up to you to implement inheritance (BaseEntity->Turret) 
#    The Turret's position is based on the location of it's owner, if it's owner (in this scenario a Tank) is moveable
#    The turret will move with it's base/owner

class Turret:
	
	def __init__(self, owner):
		self.owner = owner
		self.Position = ( 0, 0 )
		self.Rotation = 0
		self.spriteName = "./images/PlayerTanks.png"
		self.size = (29, 60 )
		self.origin = (0.55, 0.75)
		self.spriteID = AIE.CreateSprite( self.spriteName, self.size[0], self.size[1], self.origin[0], self.origin[1], 129.0/459.0, 1.0 - 61.0/158.0, 157.0/459.0, 1.0 , 0xff, 0xff, 0xff, 0xff )
		print "spriteID", self.spriteID
	
	def update(self, fDeltaTime):
		turretLocation = self.owner.getPosition()
		AIE.MoveSprite( self.spriteID, turretLocation[0], turretLocation[1] )
		
	def draw(self):
		AIE.DrawSprite( self.spriteID )
	
	def	cleanUp(self):
		AIE.DestroySprite( self.spriteID )
		