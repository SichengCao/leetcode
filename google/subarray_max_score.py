def maxscore(nums):
    n = len(nums)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+nums[i]
    print(prefix)



    res = float('-inf')
    # calculate nums[i] + nums[j] - sum(nums[i+1]+...+nums[j-1])
    # sum(nums[i+1]+...+nums[j-1]) should be prefix[j] - prefix[i+1]
    # so we should have spanning function written as nums[i] + prefix[i+1] + nums[j] - prefix[j]
    for i in range(n):
        for j in range(i+1,n):
            middle = prefix[j] - prefix[i+1]
            score = nums[i] + nums[j] - middle
            res = max(res,score)
    print(res)
    return res


def maxscore1(nums):
    n = len(nums)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+nums[i]
    print(prefix)

    res = float('-inf')
    # calculate nums[i] + nums[j] - sum(nums[i+1]+...+nums[j-1])
    # sum(nums[i+1]+...+nums[j-1]) should be prefix[j] - prefix[i+1]
    # so we should have spanning function written as nums[i] + prefix[i+1] + nums[j] - prefix[j]
    best_left = nums[0] + prefix[1]

    for j in range(1,n):
            score = best_left + nums[j] - prefix[j]
            res = max(res,score)
            best_left = max(best_left,nums[j]+prefix[j+1])
    print(res)
    return res

def maxscore1(nums):
    n = len(nums)
    prefix = [0] * (n)
    for i in range(n):
        prefix[i] += nums[i]
    print(prefix)

    res = float('-inf')
    # calculate nums[i] + nums[j] - sum(nums[i+1]+...+nums[j-1])
    # sum(nums[i+1]+...+nums[j-1]) should be prefix[j-1] - prefix[i]
    # so we should have spanning function written as nums[i] + prefix[i] + nums[j] - prefix[j-1]
    best_left = nums[0] + prefix[0]

    for j in range(1,n):
            score = best_left + nums[j] - prefix[j-1]
            res = max(res,score)
            best_left = max(best_left,nums[j]+prefix[j])
    print(res)
    return res

test_case = [3,1,2,5,4]
maxscore1(test_case)
