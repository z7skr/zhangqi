# @lc app=leetcode.cn id=35 lang=python3
# [35] 搜索插入位置
# https://leetcode.cn/problems/search-insert-position/description/
# Easy (45.04%)
# Testcase Example:  '[1,3,5,6]\n5'
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 示例 1:
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
# 提示:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 为 无重复元素 的 升序 排列数组
# -10^4 <= target <= 10^4
# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l


# @lc code=end
func = Solution().searchInsert
nums = [1, 3, 5, 6]
target = 5
print(func(nums, target))
# 输出: 2

nums = [1, 3, 5, 6]
target = 2
print(func(nums, target))
# 输出: 1

nums = [1, 3, 5, 6]
target = 7
print(func(nums, target))
# 输出: 4
