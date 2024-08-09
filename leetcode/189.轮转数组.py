# @lc app=leetcode.cn id=189 lang=python3
# [189] 轮转数组
# https://leetcode.cn/problems/rotate-array/description/
# Medium (44.51%)
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
# 提示：
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
# 进阶：
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？


# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def move(nums, k):
            def gcd(a, b):
                if a < b:
                    a, b = b, a
                while b:
                    a, b = b, a % b
                return a

            n = len(nums)
            k = k % n
            turns = gcd(k, n)  # 交换轮数
            # 每次是current的next和[start]交换, 直到回到第一次交换的位置

            # for start in range(turns):
            #     current = start
            #     next = (current + k) % n
            #     nums[next], nums[start] = nums[start], nums[next]
            #     current = next
            #     while start != current:
            #         next = (current + k) % n
            #         nums[next], nums[start] = nums[start], nums[next]
            #         current = next

            counts = n // turns - 1  # 每轮交换次数
            for start in range(turns):
                current = start
                for _ in range(counts):
                    next = (current + k) % n
                    nums[next], nums[start] = nums[start], nums[next]
                    current = next

        def reverse(nums, k):
            def reverse(a, lo, hi):
                l, r = lo, hi
                while l < r:
                    a[l], a[r] = a[r], a[l]
                    l, r = l + 1, r - 1

            n = len(nums)
            k = k % n
            reverse(nums, 0, len(nums) - 1)
            reverse(nums, 0, k - 1)
            reverse(nums, k, len(nums) - 1)

        move(nums, k)


# @lc code=end
