import math

# A* class

class AStar:
	def __init__(self):
		self.h_heuristicValue = 0
		self.g_movementCost = 0
		self.f_totalCost = 0
		self.FValue= 0
		self.HValue = 0
		self.GValue = 0
		self.n_openList = []
		self.n_closedList = []
		self.n_startNode = None
		self.n_targetNode = None
		print "A* Initialized"
		
	# Calculate F Value
	def CalculateFValue(self):
		self.f_totalCost = self.GValue - HValue
		return None