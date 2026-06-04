# Brute Force but O(N^3)

def extreme_exclusion(nums):
    n = len(nums)
    for l in range(n):
        for r in range(l + 1, n):
            sub = nums[l:r + 1]

            mn = min(sub)
            mx = max(sub)

            if nums[l] != mn and nums[l] != mx and \
                    nums[r] != mn and nums[r] != mx:
                return (l, r)
    return -1


# Brute Force but O(N^2)

def extreme_exclusion1(nums):
    n = len(nums)
    for l in range(n):
        mn = nums[l]
        mx = nums[l]
        for r in range(l + 1, n):
            mn = min(mn,nums[r])
            mx = max(mx,nums[r])

            if nums[l] != mn and nums[l] != mx and \
                    nums[r] != mn and nums[r] != mx:
                return (l, r)
    return -1


def extreme_exclusion2(nums):
    n = len(nums)

    sorted_vals = sorted(nums)
    rank = {v: i for i, v in enumerate(sorted_vals)}
    print("rank: ", rank)
    arr = [rank[x] for x in nums]
    print(arr)

    alive = set(arr)
    print(alive)

    l, r = 0, n - 1
    mn, mx = 0, n - 1

    while l < r:
        if mn not in alive:
            mn += 1
        if mx not in alive:
            mx -= 1

        if arr[l] == mn or arr[l] == mx:
            alive.remove(arr[l])
            l += 1
        elif arr[r] == mn or arr[r] == mx:
            alive.remove(arr[r])
            r -= 1
        else:
            return [l, r]

    return None

#
nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]
nums1 = [4,2,5,1,3]
print(extreme_exclusion2(nums))
