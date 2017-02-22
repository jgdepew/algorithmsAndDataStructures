def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    while k > 0:
        nums.insert(0, nums.pop())
        k -= 1


nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print nums