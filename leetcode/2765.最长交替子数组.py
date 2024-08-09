# @lc app=leetcode.cn id=2765 lang=python3
# [2765] 最长交替子数组
# https://leetcode.cn/problems/longest-alternating-subarray/description/
# Easy (48.24%)
# Testcase Example:  '[2,3,4,3,4]'
# 给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：
# m 大于 1 。
# s1 = s0 + 1 。
# 下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 -
# s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)^m 。
# 请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。
# 子数组是一个数组中一段连续 非空 的元素序列。
# 示例 1：
# 输入：nums = [2,3,4,3,4]
# 输出：4
# 解释：交替子数组有 [3,4] ，[3,4,3] 和 [3,4,3,4] 。最长的子数组为 [3,4,3,4] ，长度为4 。
# 示例 2：
# 输入：nums = [4,5,6]
# 输出：2
# 解释：[4,5] 和 [5,6] 是仅有的两个交替子数组。它们长度都为 2 。
# 提示：
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
from typing import *


# @lc code=start
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        # dp[i]: 以 nums[i] 为结尾的最长交替子数组
        def f1(nums):
            if len(nums) <= 1:
                return -1
            dp = [0] * len(nums)
            dp[1] = 2 if nums[1] - nums[0] == 1 else 0
            for i in range(2, len(nums)):
                if dp[i - 1] > 0 and nums[i] == nums[i - 2]:
                    dp[i] = dp[i - 1] + 1
                elif nums[i] - nums[i - 1] == 1:
                    dp[i] = 2
                else:
                    dp[i] = 0
            res = max(dp)
            return -1 if res == 0 else res
            # nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

        # dp 优化
        def f2(nums):
            # dp数组只用到了dp[i-1], 可以简化为单个变量
            if len(nums) <= 1:
                return -1
            dp = 2 if nums[1] - nums[0] == 1 else 0
            res = dp
            for i in range(2, len(nums)):
                if dp > 0 and nums[i] == nums[i - 2]:
                    dp = dp + 1
                elif nums[i] - nums[i - 1] == 1:
                    dp = 2
                else:
                    dp = 0
                res = max(res, dp)
            return -1 if res == 0 else res

        return f1(nums)


# @lc code=end

func = Solution().alternatingSubarray
nums = [2, 3, 4, 3, 4]
print(func(nums))
