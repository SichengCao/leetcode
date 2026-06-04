def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    a = 0
    b = 0
    while a < len(nums):
        if nums[a] != val:
            nums[b] = nums[a]
            b += 1
        a += 1
    
    return b


n = [3, 2, 2, 3]
v = 3

res = removeElement(n, v)
print(n)
print(res)
