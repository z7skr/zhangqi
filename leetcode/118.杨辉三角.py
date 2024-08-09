# @lc app=leetcode.cn id=118 lang=python3
# [118] 杨辉三角
# https://leetcode.cn/problems/pascals-triangle/description/
# Easy (75.86%)
# Testcase Example:  '5'
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例 2:
# 输入: numRows = 1
# 输出: [[1]]
# 提示:
# 1


# @lc code=start
class Solution:
    from typing import List

    def generate(self, numRows: int) -> List[List[int]]:
        return self.generate_遍历(numRows)

    def generate_递归(self, numRows: int) -> List[List[int]]:
        pass

    def generate_遍历(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            nums = res[-1]
            mid = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]
            res.append([nums[0]] + mid + [nums[-1]])
        return res


# @lc code=end


func = Solution().generate
numRows = 1
print(func(numRows))
#  [[1]]

numRows = 2
print(func(numRows))
#  [[1],[1,1]]

numRows = 5
print(func(numRows))
#  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
