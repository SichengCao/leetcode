# search the number
def binarySearch1(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


# find the first number which is greater than target
def binarySearch2(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        # if nums[mid] == target:
        #     return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

#find the peakvalue
def binarySearch3(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left+right)//2

        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return left





res = binarySearch2([1, 2, 3, 4, 5], 3)

peak_val = binarySearch3([1,3,5,7,6])
print(peak_val)
print(res)
