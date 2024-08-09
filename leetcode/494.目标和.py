# @lc app=leetcode.cn id=494 lang=python3
# [494] 目标和
# https://leetcode.cn/problems/target-sum/description/
# Medium (48.41%)
# Testcase Example:  '[1,1,1,1,1]\n3'
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 示例 1：
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1
# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, target):
            if i == len(nums):
                return 1 if target == 0 else 0
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i + 1, target - nums[i])] = dp(i + 1, target - nums[i])
            memo[(i + 1, target + nums[i])] = dp(i + 1, target + nums[i])
            return memo[(i + 1, target - nums[i])] + memo[(i + 1, target + nums[i])]

        return dp(0, target)


# @lc code=end
f = Solution().findTargetSumWays
nums = [1, 1, 1, 1, 1]
target = 3
print(f(nums, target))

nums = [1]
target = 1
print(f(nums, target))

nums = [20, 27, 22, 23, 0, 44, 22, 44, 39, 7, 35, 23, 17, 30, 37, 4, 14, 42, 31, 43]
target = 38
print(f(nums, target))
