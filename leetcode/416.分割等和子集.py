# @lc app=leetcode.cn id=416 lang=python3
# [416] 分割等和子集
# https://leetcode.cn/problems/partition-equal-subset-sum/description/
# Medium (52.54%)
# Testcase Example:  '[1,5,11,5]'
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
# 提示：
# 1
# 1

# @lc code=start
class Solution:
    from typing import List
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        if n < 2 or s & 1 or max(nums) > s // 2:
            return False
        target = s // 2

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - num]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n-1][target]

            
        
# @lc code=end

func = Solution().canPartition
nums = [1,5,11,5]
print(func(nums))
# true

nums = [1,2,3,5]
print(func(nums))
# false

