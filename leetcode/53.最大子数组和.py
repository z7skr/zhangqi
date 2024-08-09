# @lc app=leetcode.cn id=53 lang=python3
# [53] 最大子数组和
# https://leetcode.cn/problems/maximum-subarray/description/
# Medium (55.16%)
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
# 提示：
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dp1():
            # dp[i]: 以nums[i]结尾的最大连续数组和
            dp = [0] * len(nums)
            for i in range(1, len(nums)):
                dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxSum = max(dp)
            return maxSum

        def dp2():
            curSum = maxSum = nums[0]
            for num in nums[1:]:
                curSum = max(curSum + num, num)
                maxSum = max(maxSum, curSum)
            return maxSum

        def dc():
            def max_sub_array(nums, left, right):
                if left == right:
                    return nums[left]
                mid = (left + right) >> 1
                # 包含 mid 的最大子数组和
                left_sum_max, right_sum_max, left_sum, right_sum = 0, 0, 0, 0
                for start_left in reversed(range(left, mid)):
                    left_sum += nums[start_left]
                    left_sum_max = max(left_sum_max, left_sum)
                for start_right in range(mid + 1, right + 1):
                    right_sum += nums[start_right]
                    right_sum_max = max(right_sum_max, right_sum)
                max_cross_array = left_sum_max + nums[mid] + right_sum_max

                return max(
                    max_sub_array(nums, left, mid),
                    max_sub_array(nums, mid + 1, right),
                    max_cross_array,
                )

            return max_sub_array(nums, 0, len(nums) - 1)

        return dc()


# @lc code=end

func = Solution().maxSubArray

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(func(nums))
# 输出：6

nums = [1]
print(func(nums))
# 输出：1

nums = [5, 4, -1, 7, 8]
print(func(nums))
# 输出：23
