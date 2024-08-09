# @lc app=leetcode.cn id=152 lang=python3
# [152] 乘积最大子数组
# https://leetcode.cn/problems/maximum-product-subarray/description/
# Medium (43.16%)
# Testcase Example:  '[2,3,-2,4]'
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。
# 示例 1:
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 提示:
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数


# @lc code=start
from functools import reduce
import operator


class Solution:
    from typing import List

    def maxProduct(self, nums: List[int]) -> int:
        def recursive():
            def maxprodnonzero(nums):
                n = len(nums)
                if n == 1:
                    return nums[0]
                n_neg = sum([num < 0 for num in nums])
                PROD = reduce(operator.mul, nums)
                if n_neg & 1 == 0:
                    return PROD
                else:
                    left, right = 1, 1
                    for i in range(n):
                        if left > 0:
                            left *= nums[i]
                        if right > 0:
                            right *= nums[n - 1 - i]
                    return PROD // max(left, right)

            def recursive(nums):
                if 0 not in nums:
                    return maxprodnonzero(nums)
                i = nums.index(0)
                r = 0
                if i > 0:
                    r = max(r, maxprodnonzero(nums[:i]))
                if i + 1 < len(nums):
                    r = max(r, recursive(nums[i + 1 :]))
                return r

            return recursive(nums)

        def best():
            if not nums:
                return 0
            max_prod = prev_max = prev_min = nums[0]
            for i in range(1, len(nums)):
                curr_min = min(prev_min * nums[i], prev_max * nums[i], nums[i])
                curr_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
                prev_min, prev_max = curr_min, curr_max
                max_prod = max(max_prod, curr_max)
            return max_prod
        
        def dp():
            dp_min = nums[:]
            dp_max = nums[:]
            for i in range(1, len(nums)):
                dp_min[i] = min(nums[i], dp_min[i-1] * nums[i], dp_max[i-1] * nums[i])
                dp_max[i] = max(nums[i], dp_min[i-1] * nums[i], dp_max[i-1] * nums[i])
            return max(dp_min + dp_max)
        
        return best()


# @lc code=end


func = Solution().maxProduct
nums = [2, 3, -2, 4]
print(func(nums))
#  6

nums = [-2, 0, -1]
print(func(nums))
#  0

nums = [0, 2, 0, 2]
print(func(nums))
#  2
