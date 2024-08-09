# @lc app=leetcode.cn id=33 lang=python3
# [33] 搜索旋转排序数组
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
# Medium (44.39%)
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
# 提示：
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4


# @lc code=start
class Solution:
    from typing import List

    def search(self, nums: List[int], target: int) -> int:
        def bisearch(nums, lo, hi):
            while lo <= hi:
                mid = (lo + hi) >> 1
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    return mid
            return -1

        def dfs(lo: int, hi: int):
            mid = (lo + hi) >> 1
            if lo > hi:
                return -1
            if nums[lo] <= nums[hi]:
                return bisearch(nums, lo, hi)
            if nums[hi] < target < nums[lo]:
                return -1
            left = dfs(lo, mid)
            if left > -1:
                return left
            return dfs(mid + 1, hi)

        # return dfs(0, len(nums) - 1)

        def best():
            if not nums:
                return -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[0] <= nums[mid]:
                    if nums[0] <= target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if nums[mid] < target <= nums[len(nums) - 1]:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1

        return best()


# @lc code=end


func = Solution().search
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(func(nums, target))
# 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
print(func(nums, target))
# 1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(func(nums, target))
# 5

nums = [3, 5, 1]
target = 5
print(func(nums, target))
# 1
