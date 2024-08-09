# @lc app=leetcode.cn id=34 lang=python3
# [34] 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Medium (43.67%)
# Testcase Example:  '[5,7,7,8,8,10]\n8'
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 提示：
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9


# @lc code=start
class Solution:
    from typing import List

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_first(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo if nums[lo] == target else -1

        def search_last(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi + 1) >> 1
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    lo = mid
            return -1 if lo >= len(nums) or nums[lo] != target else lo

        if not nums:
            return [-1, -1]
        # first = search_first(nums, target)
        # if first == -1:
        #     return [first, first]
        # return [first, search_last(nums, target)]

        return [search_first(nums, target), search_last(nums, target)]


# @lc code=end


func = Solution().searchRange
nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8
print(func(nums, target))
# [3, 6]

nums = [5, 7, 7, 8, 8, 10]
target = 6
print(func(nums, target))
# [-1,-1]

nums = [1]
target = 0
print(func(nums, target))
# [-1,-1]

nums = [2, 2]
target = 3
print(func(nums, target))
# [-1,-1]
