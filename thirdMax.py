# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

def thirdMax(nums):

    numbers = set(nums)
    print numbers
    results = []
    for i in xrange(len(nums)):
        maximum = max(numbers)
        results.append(maximum)
        numbers.remove(maximum)
        if len(results) == 3 or len(numbers) == 0:
            break
        
    print results
    if len(results) == 3:
        return min(results)
    else:
        return max(results)

nums = [1,1,2]

print thirdMax(nums)



