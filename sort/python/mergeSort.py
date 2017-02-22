import random

def mergeSort(arr):
	if len(arr) < 2:
		return arr

	half = len(arr)/2
	left = mergeSort(arr[:half])
	right = mergeSort(arr[half:])

	return merge(left, right)

def merge(left, right):
	if not len(left) or not len(right):
		return right or left

	results = []
	i, j = 0, 0

	while len(results) < len(left) + len(right):
		if left[i] < right[j]:
			results.append(left[i])
			i += 1
		else:
			results.append(right[j])
			j += 1

		if len(left) == i or len(right) == j:
			results.extend(right[j:] or left[i:])
			break

	return results

def fillArray():
	arr = []
	for i in xrange(10):
		arr.append(random.randrange(100))
	return arr

arr = fillArray()
print arr
arr = mergeSort(arr)
print arr