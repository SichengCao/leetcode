from collections import defaultdict


def check(nums1,nums2,D):

    map1 = defaultdict(list)
    map2 = defaultdict(list)

    for i,v in enumerate(nums1):
        if v!=0:
            map1[v].append(i)

    print(map1)

    for i, v in enumerate(nums2):
        if v != 0:
            map2[v].append(i)

    print(map2)
    res = list()
    for item in map1:

        if item not in map2:
            continue

        arr1 = map1[item]
        arr2 = map2[item]

        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(arr1) and pointer2 < len(arr2):
            a = arr1[pointer1]
            b = arr2[pointer2]

            if abs(a-b) <=D:
                res.append(item)
                break

            if a < b:
                pointer1+=1
            else:
                pointer2+=2
    return res






A = [0, 5, 0, 5, 0, 5, 9, 0, 9]

B = [5, 0, 0, 5, 9, 0, 0, 5, 0]

D = 2

res = check(A,B,D)
print(res)