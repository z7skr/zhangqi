# @lc app=leetcode.cn id=440 lang=python3
# [440] 字典序的第K小数字
# https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/description/
# Hard (42.37%)
# Testcase Example:  '13\n2'
# 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
# 示例 1:
# 输入: n = 13, k = 2
# 输出: 10
# 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
# 示例 2:
# 输入: n = 1, k = 1
# 输出: 1
# 提示:
# 1 <= k <= n <= 10^9

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        pass
# @lc code=end


func = Solution().findKthNumber
n = 13
k = 2
print(func(n, k))
#  10

n = 1
k = 1
print(func(n, k))
#  1

