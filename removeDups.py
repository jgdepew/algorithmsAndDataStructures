# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

def removeDups(nums):
	i = 0
	while i < len(nums)-1:
		if nums[i] == nums[i+1]:
			del nums[i]
		else:
			i += 1
	return nums

nums = []
for i in xrange(-10000):
	nums.append(i)
	nums.append(i)

print removeDups(nums)