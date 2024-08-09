# @lc app=leetcode.cn id=238 lang=python3
# [238] 除自身以外数组的乘积
# https://leetcode.cn/problems/product-of-array-except-self/description/
# Medium (75.10%)
# Testcase Example:  '[1,2,3,4]'
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
# 提示：
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def brute_force(nums):
            length = len(nums)
            res = [1] * length
            for i in range(length):
                for j in range(length):
                    if i == j:
                        continue
                    res[i] *= nums[j]
            return res

        def assist_array(nums):
            length = len(nums)
            L = [1] * length
            for i in range(1, length):
                L[i] = L[i - 1] * nums[i - 1]
            R = [1] * length
            for i in reversed(range(length - 1)):
                R[i] = R[i + 1] * nums[i + 1]
            res = [1] * length
            for i in range(length):
                res[i] = L[i] * R[i]
            return res

        def O1(nums):
            # 把 L 作为返回数组先求出来, R 不作为数组而是每个当前值, 依次计算 R, 同时更新 L
            length = len(nums)
            L = [1] * length
            for i in range(1, length):
                L[i] = L[i - 1] * nums[i - 1]
            R = 1
            for i in reversed(range(length - 1)):
                R = R * nums[i + 1]
                L[i] = L[i] * R
            return L

        return O1(nums)


# @lc code=end
