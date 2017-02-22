import random

# *********************************************************

# BST

# time complexity: 
	# Best: O(log n)
	# Worst: O(n)


# space complexity:
	# Worst: O(n)
	# Best: O(n)

class Node(object):
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

class BST(object):
	def __init__(self):
		self.head = None
	
	def fill(self):
		for i in xrange(20):
			self.add(random.randrange(-30, 30))
		return self

	def printTree(self, node): # in ascending order
		if not node:
			return
		self.printTree(node.left)
		print node.val
		self.printTree(node.right)

		# return 

	def add(self, val):
		newNode = Node(val, None, None)
		if not self.head:
			self.head = newNode
			return self
		current = self.head
		while current:
			if val < current.val:
				if not current.left:
					current.left = newNode
					return self
				else:
					current = current.left
			elif val > current.val:
				if not current.right:
					current.right = newNode
					return self
				else:
					current = current.right
			else:
				return self

	def height(self, node):
		if not node:
			return 0
		left = self.height(node.left)
		right = self.height(node.right)
		return max(left, right) + 1

	def count(self, node):
		if not node:
			return 0
		left = self.count(node.left) 
		right = self.count(node.right) 
		return (left+right) + 1

	def searchNode(self, val, node):
		if not node: 
			return False
		if node.val == val:
			return True
		if val < node.val: 
			result = self.searchNode(val, node.left) 
		else:
			result = self.searchNode(val, node.right)
		if result:
			return True
		return False

	def searchMin(self, node):
		if node.left == None:
			return node
		return self.searchMin(node.left)

	def searchMax(self, node):
		if node.right == None:
			return node
		return self.searchMax(node.right)

	def isValid(self, node, minVal, maxVal): # initiate with minVal = float('inf')*-1 and maxVal = float('inf')
		if not node:
			return True
		if node.val < minVal or node.val > maxVal:
			return False
		return self.isValid(node.right, node.val, maxVal) and self.isValid(node.left, minVal, node.val)

	def getSuccessor(self, val): # returns next-highest value in tree after given value, -1 if none
		if not self.head:
			return -1
		greater = self.searchMax(self.head)
		if greater < val:
			return -1
		current = self.head
		while current:
			if val < current.val and greater > current.val:
				greater = current.val
			if val<current.val:
				current = current.left
			else:
				current = current.right
		return greater

	def deleteNode(self, val):
		if self.head.val != val:
			if self.head.left:
				left = self.rDelete(val, self.head.left, self.head)
				if left:
					return True
			if self.head.right:
				right = self.rDelete(val, self.head.right, self.head)
				if right:
					return True
			return False
		left = self.height(self.head.left)
		right = self.height(self.head.right)
		if left > right:
			current = self.head.left
			while current.right.right:
				current = current.right
			temp = current.right
			current.right = None
		else:
			current = self.head.right
			while current.left.left:
				current = current.left
			temp = current.left
			current.left = None
		temp.left = self.head.left
		temp.right = self.head.right
		self.head.right = None
		self.head.left = None
		self.head = temp

	def rDelete(self, val, node, parent):
		if not node:
			return self
		if val == node.val: 
			if node.left and node.right:
				return self.delete2Children(val, node, parent)
			if node.left or node.right:
				return self.delete1Child(val, node, parent)
			if not node.left and not node.right:
				return self.delete0Children(val, node, parent)
		if node.right:
			right = self.rDelete(val, node.right, node)
			if right:
				return True
		if node.left:
			left = self.rDelete(val, node.left, node)
			if left: 
				return True

	def delete0Children(self, val, node, parent):
		if parent.left == node:
			parent.left = None
			return True
		if parent.right == node:
			parent.right = None
			return True

	def delete1Child(self, val, node, parent):
		if parent.left == node:
			if node.left != None:
				parent.left = node.left
				node.left = None
			if node.right != None:
				parent.left = node.right
				node.right = None
			return True
		if parent.right == node:
			if node.left != None:
				parent.right = node.left
				node.left = None
			if node.right != None:
				parent.right = node.right
				node.right = None
			return True

	def delete2Children(self, val, node, parent):
		left = self.height(node.left)
		right = self.height(node.right)
		child = ""
		if parent.left == node:
			child = "left"
		else:
			child = "right"
		if left > right:
			current = node.left
			while current.right.right:
				current = current.right
			temp = current.right
			current.right = None
		else:
			current = node.right
			while current.left.left:
				current = current.left
			temp = current.left
			current.left = None
		temp.left = node.left
		temp.right = node.right
		node.right = None
		node.left = None
		if child == "left":
			parent.left = temp
		else:
			parent.right = temp
		return True







