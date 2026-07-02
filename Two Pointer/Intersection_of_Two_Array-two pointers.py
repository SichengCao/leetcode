nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    point1 = 0
    point2 = 0
    res = []
    while point1 < len(nums1) and point2 < len(nums2):

        if nums1[point1] == nums2[point2]:
            res.append(nums1[point1])
            point1 += 1
            point2 += 1
        elif nums1[point1] < nums2[point2]:
            point1 += 1
        else:
            point2 += 1

    return res


print(intersect(nums1, nums2))
