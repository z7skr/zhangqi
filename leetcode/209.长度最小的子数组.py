# @lc app=leetcode.cn id=209 lang=python3
# [209] 长度最小的子数组
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
# Medium (46.43%)
# Testcase Example:  '7\n[2,3,1,2,4,3]'
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 示例 1：
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 提示：
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 进阶：
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 总和大于等于target的最短子数组长度,else 0
        res = len(nums) + 1
        summ = 0
        left, right = 0, 0
        while right < len(nums):
            # 扩大窗口
            num = nums[right]
            right += 1
            # do
            summ += num
            # 缩小窗口
            while summ >= target:
                # 判断
                res = min(res, right - left)
                # 缩小窗口
                num = nums[left]
                left += 1
                # do
                summ -= num

        return 0 if res == len(nums) + 1 else res


# @lc code=end
