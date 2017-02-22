# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

def missingNumber(self, nums):

    sum = 0
    realSum = 0
    minimum = min(nums)
    maximum = max(nums)
    for i in xrange(len(nums)):
        sum += nums[i]
        realSum += i
        
    realSum += len(nums)
    
    difference = abs(realSum - sum)

    if minimum != 0:
        return 0
    elif maximum != len(nums):
        return len(nums)
    else:
        return difference