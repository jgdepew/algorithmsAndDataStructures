#
#		   B   D
#		  /   /
#head->  A   C----E
#		  \ / \   |
#		   S   F  |
#			\ /   |
#			 G----H
#

class GraphNode(object):
	def __init__(self, idx, val):
		self.idx = idx
		self.val = val
		self.searched = False

class EdgeNode(object):
	def __init__(self, node, weight):
		self.node = node
		self.weight = weight

class AdjacencyList(object):
	def __init__(self):
		self.vertexes = []
		self.adjacencyList = []

	def addVertex(val):

