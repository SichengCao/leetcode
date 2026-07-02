# class Solution:
#     def __init__(self):
#         self.path = []
#         self.paths = []
#
#     def permute(self, nums):
#
#         self.backtracking(nums)
#         return self.paths
#
#     def backtracking(self, nums):
#
#         if len(self.path) == 2:
#             self.paths.append(self.path[:])
#             return
#
#         for i in range(0, len(nums)):
#             self.path.append(nums[i])
#             self.backtracking(nums)
#             self.path.pop()


# res = Solution()
# res1 = res.permute(['+', '-', '*', '/'])


res1 = [['+', '+'], ['+', '-'], ['+', '*'], ['+', '/'], ['-', '+'], ['-', '-'], ['-', '*'], ['-', '/'], ['*', '+'], ['*', '-'], ['*', '*'], ['*', '/'], ['/', '+'], ['/', '-'], ['/', '*'], ['/', '/']]

numlist = input().split(' ')

num1 = numlist[0]
num2 = numlist[1]
num3 = numlist[2]

output_list = []
for item in res1:
    temp = 0
    if item[0] == '+':
        temp = int(num1) + int(num2)
    if item[0] == '-':
        temp = int(num1) - int(num2)
    if item[0] == '*':
        temp = int(num1) * int(num2)
    if item[0] == '/':
        temp = int(num1) / int(num2)

    if temp % 1 != 0:
        continue
    else:
        if item[1] == '+':
            temp += int(num3)
        if item[1] == '-':
            temp -= int(num3)
        if item[1] == '*':
            temp *= int(num3)
        if item[1] == '/':
            temp /= int(num3)
        output_list.append(temp)

new_list = []
for item in output_list:
    if item < 0 or item % 1 != 0:
        continue
    else:
        new_list.append(int(item))

print(min(new_list))


