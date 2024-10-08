# @lc app=leetcode.cn id=873 lang=python3
# [873] 最长的斐波那契子序列的长度
# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/description/
# Medium (56.16%)
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
# n >= 3
# 对于所有 i + 2 ，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
# （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8]
# 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
# 示例 1：
# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
# 示例 2：
# 输入: arr = [1,3,7,11,12,14,18]
# 输出: 3
# 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
# 提示：
# 3
# 1


# @lc code=start
class Solution:
    from typing import List

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = [{} for _ in range(len(arr))]  # dp[i][k]: [arr[i], k] 的fib数列
        res = 0
        for i in range(len(arr)):
            for j in range(i):
                pre_num = arr[i] - arr[j]
                dp[i][arr[j]] = dp[i].get(arr[j], dp[j].get(pre_num, 1)) + 1
                res = max(res, dp[i][arr[j]])
        return res if res >= 3 else 0


# @lc code=end


func = Solution().lenLongestFibSubseq
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(func(arr))
#  5

arr = [1, 3, 7, 11, 12, 14, 18]
print(func(arr))
#  3

arr = [1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 21]
print(func(arr))
#  7

arr = [1, 2, 3]
print(func(arr))
#  3

arr = [1, 3, 5]
print(func(arr))
#  0
