# @lc app=leetcode.cn id=119 lang=python3
# [119] 杨辉三角 II
# https://leetcode.cn/problems/pascals-triangle-ii/description/
# Easy (69.00%)
# Testcase Example:  '3'
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:
# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:
# 输入: rowIndex = 1
# 输出: [1,1]
# 提示:
# 0
# 进阶：
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？


# @lc code=start
class Solution:
    from typing import List

    def getRow(self, rowIndex: int) -> List[int]:
        # ans[i+1] = nC(i+1) = n!/[(i-1)!*(n-i+1)!] = n!/[i!*(n-i)!/i*(n-i+1)]
        #          = nCi / i * (n-i+1) = ans[i] / i * (n-i+1)
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            ans[i] = ans[i - 1] * (rowIndex - i + 1) // i
        return ans


# @lc code=end


func = Solution().getRow
rowIndex = 0
print(func(rowIndex))
#  [1]

rowIndex = 1
print(func(rowIndex))
#  [1,1]

rowIndex = 2
print(func(rowIndex))
#  [1,2,1]

rowIndex = 3
print(func(rowIndex))
#  [1,3,3,1]

rowIndex = 4
print(func(rowIndex))
#  [1,4,6,4,1]
