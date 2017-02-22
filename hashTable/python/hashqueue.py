# This file is used to implement the breadth first and depth first searches
# This is also a linked list

class QueueNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue(object):
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head

	def enqueue(self, val):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = QueueNode(val)
		else:
			self.head = QueueNode(val)
		return self

	def dequeue(self):
		if self.head:
			temp = self.head
			self.head = self.head.next
			return temp.val
		return None

	def isEmpty(self):
		return self.head == None

	def searchQueue(self, val):
		if self.head:
			current = self.head
			while current:
				if current.val == val:
					return current
				current = current.next
		return False

	def removeFromQueue(self, val):
		if self.head:
			if self.head.val == val:
				temp = self.head
				self.head = temp.next
				temp.next = None
				return temp
				
			current = self.head
			while current.next:
				if current.next.val == val:
					temp = current.next
					current.next = temp.next
					temp.next = None
					return temp
		return False

	def toString(self):
		if self.head:
			current = self.head
			while current:
				print current.val,
				current = current.next
			print "\n"
		return self

# queue = Queue()
# queue.enqueue(3).enqueue(7).enqueue(4).enqueue(1).enqueue(8).enqueue(9).enqueue(2).enqueue(0)
# queue.toString()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.toString()