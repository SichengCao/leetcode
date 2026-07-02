import math


class Solution:

    # def minEatingSpeed(self, piles, h):
    #
    #     left = 1
    #     right = max(piles)
    #
    #     while left < right:
    #
    #         mid = (left + right) // 2
    #
    #         total_hours = 0
    #
    #         for pile in piles:
    #
    #             total_hours += math.ceil(pile / mid)
    #
    #         if total_hours <= h:
    #             right = mid
    #         else:
    #             left = mid + 1
    #
    #     return left

    def minEatingSpeed(self, piles, h):

        left  = 1
        right = max(piles)

        while left < right:

            mid = (left+right)//2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/mid)

            if total_hours <= h:
                right = mid
            else:
                left = mid+1

        return left




piles = [3, 6, 7, 11]
h = 8

sol = Solution()

answer = sol.minEatingSpeed(piles, h)

print("Minimum eating speed:", answer)