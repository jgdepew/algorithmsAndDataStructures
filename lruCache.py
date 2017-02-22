# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.items = {}
        self.numItems = 0
        self.recent = Queue()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if str(key) in self.items:
            self.updateRecent(key)
            return self.items[str(key)]
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if str(key) not in self.items and self.numItems != self.capacity:
            self.items[str(key)] = value
            self.numItems += 1
        elif str(key) not in self.items and self.capacity == self.numItems:
            self.removeLeastRecent(key)
            self.items[str(key)] = value
        elif str(key) in self.items:
            self.items[str(key)] = value
            
        self.updateRecent(key)
            
    def removeLeastRecent(self, key):
    	remove = self.recent.dequeue()
        del self.items[str(remove)]
    
    def updateRecent(self, key):
        self.recent.removeValue(key)
        self.recent.enqueue(key)
        return key

class QueueNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue(object):
	def __init__(self):
		self.head = None

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

	def removeValue(self, val):
		if self.head:
			if self.head.val == val:
				return self.dequeue()
			current = self.head
			while current.next:
				if current.next.val == val:
					temp = current.next
					current.next = temp.next
					temp.next = None
					return temp.val
				current = current.next
		return False
        