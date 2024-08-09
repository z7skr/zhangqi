# @lc app=leetcode.cn id=1027 lang=python3
# [1027] 最长等差数列
# https://leetcode.cn/problems/longest-arithmetic-subsequence/description/
# Medium (49.48%)
# Testcase Example:  '[3,6,9,12]'
# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... <
# ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1)
# 的值都相同，那么序列 seq 是等差的。
# 示例 1：
# 输入：nums = [3,6,9,12]
# 输出：4
# 解释：
# 整个数组是公差为 3 的等差数列。
# 示例 2：
# 输入：nums = [9,4,7,2,10]
# 输出：3
# 解释：
# 最长的等差子序列是 [4,7,10]。
# 示例 3：
# 输入：nums = [20,1,15,3,10,5,8]
# 输出：4
# 解释：
# 最长的等差子序列是 [20,15,10,5]。
# 提示：
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


# @lc code=start
class Solution:
    from typing import List

    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        dp = [{} for _ in range(n)]
        # dp[i][k] 表示以 nums[i] 为结尾的 diff = k 的子序列长度
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
        return res


# @lc code=end


func = Solution().longestArithSeqLength
nums = [3, 6, 9, 12]
print(func(nums))
# 4

nums = [9, 4, 7, 2, 10]
print(func(nums))
# 3

nums = [20, 1, 15, 3, 10, 5, 8]
print(func(nums))
# 4
