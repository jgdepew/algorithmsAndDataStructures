def delete(self, val):
	if not self.head:
		return False
	if self.head.val != val:
		left = self.rDelete(self, val, self.head.left, self.head)
		if left:
			return left
		right = self.rDelete(self, val, self.head.right, self.head)
		if right:
			return right
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
