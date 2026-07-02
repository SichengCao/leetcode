# class Solution:
#
#     def maxSumIntervals(self, nums):
#
#         n = len(nums)
#
#         if n == 0:
#             return (0, 0)
#
#         # -------------------------
#         # build prefix sum
#         # prefix[k] = sum(nums[0:k])
#         # -------------------------
#         prefix = [0] * n
#         prefix[0] = nums[0]
#         for i in range(1,n):
#             prefix[i] = prefix[i-1] + nums[i]
#
#         best_sum = float('-inf')
#         ans = (0, 0)
#
#         # -------------------------
#         # enumerate all pairs
#         # -------------------------
#         for i in range(n):
#
#             for j in range(i, n):
#
#                 if nums[i] == nums[j]:
#
#                     # subarray sum
#                     cur_sum = prefix[j] - prefix[i-1]
#
#                     if cur_sum > best_sum:
#                         best_sum = cur_sum
#                         ans = (i, j)
#
#         return ans

class Solution:

    def maxSumIntervals(self, nums):

        n = len(nums)

        if n == 0:
            return (0, 0)

        # -----------------------------------
        # prefix[i]
        # =
        # sum(nums[0...i])
        # -----------------------------------
        prefix = [0] * n

        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # -----------------------------------
        # seen[value]
        # =
        # (
        #   minimum prefix before this value,
        #   corresponding index
        # )
        # -----------------------------------
        seen = {}

        best_sum = float('-inf')

        ans = (0, 0)

        # -----------------------------------
        # iterate each position as right end
        # -----------------------------------
        for j in range(n):

            val = nums[j]

            # -----------------------------------
            # if same value appeared before,
            # calculate candidate subarray sum
            # -----------------------------------
            if val in seen:

                min_prefix_before_i, i = seen[val]

                # sum(i...j)
                cur_sum = prefix[j] - min_prefix_before_i

                if cur_sum > best_sum:

                    best_sum = cur_sum

                    ans = (i, j)

            # -----------------------------------
            # if current j becomes future i,
            # we need prefix[i-1]
            # -----------------------------------
            before_i = 0 if j == 0 else prefix[j - 1]

            # -----------------------------------
            # keep the smallest prefix
            # because:
            #
            # prefix[j] - prefix[i-1]
            #
            # is maximized when:
            #
            # prefix[i-1] is minimized
            # -----------------------------------
            if val not in seen or before_i < seen[val][0]:

                seen[val] = (before_i, j)

        return ans


# -----------------------------------
# example
# -----------------------------------
nums = [1, 2, 3, 2, 5]

sol = Solution()

print(sol.maxSumIntervals(nums))