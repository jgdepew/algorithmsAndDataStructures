from hashqueue import Queue, QueueNode
# Hash Tables

class HashTable(object):
	def __init__(self, capacity = 10):
		# capacity initialized to 1000
		self.capacity = capacity
		self.size = 0
		self.table = [None] * capacity

	def hashFunction(self, val):
		return val % self.capacity

	def add(self, val):
		key = self.hashFunction(val)
		if self.table[key] == None:
			queue = Queue()
			self.table[key] = queue
		else:
			queue = self.table[key]

		queue.enqueue(val)
		self.size += 1
		return self

	def search(self, val):
		key = self.hashFunction(val)
		if self.table[key] != None:
			queue = self.table[key]
			result = queue.searchQueue(val)
			return result.val
		return self.table[key]

	def remove(self, val):
		key = self.hashFunction(val)
		if self.table[key] != None:
			queue = self.table[key]
			result = queue.removeFromQueue(val)
			if result:
				self.size -= 1
				if queue.head == None:
					self.table[key] = None
				return result
		return False

	def printTable(self):
		count = 0
		for i in self.table:
			print "AT INDEX", count, ":"
			if i:
				i.toString()
			count += 1



# ht = HashTable()
# ht.add(5).add(15).add(23).add(28).add(39).add(18).add(14)
# ht.printTable()
# print "SIZE:", ht.size
# print ht.search(28)
# print ht.remove(39).val
# ht.printTable()
# print "SIZE:", ht.size

