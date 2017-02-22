# time complexity: 
	# Worst: O(n)
	# Best: O(log n)


# space complexity:
	# Worst: O(n)
	# Best: O(n)

def binarySearch(val, arr):
	lo, hi = 1, len(arr)
	while lo <= hi:
		mid = lo + (hi-lo)/2
		if arr[mid] == val:
			return mid
		elif arr[mid] < val:
			lo = mid + 1
		else:
			hi = mid - 1
		if hi == 0 or lo == len(arr):
			return False



arr = [17, 38, 44, 56, 63, 67, 73, 80, 95, 98]
print binarySearch(98, arr)
