# Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
	dict = {};
	difference = 0
	for i in xrange(len(nums)):
		if str(nums[i]) not in dict: 
			difference = target - nums[i]
			dict[str(difference)] = i
		else: 
			return [dict[str(nums[i])], i]
		


nums = [3,3]

print twoSum(nums, 6)