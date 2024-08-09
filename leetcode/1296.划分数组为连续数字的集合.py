# @lc app=leetcode.cn id=1296 lang=python3
# [1296] 划分数组为连续数字的集合
# https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
# Medium (49.61%)
# Testcase Example:  '[1,2,3,3,4,4,5,6]\n4'
# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
# 如果可以，请返回 true；否则，返回 false。
# 示例 1：
# 输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
# 示例 2：
# 输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
# 示例 3：
# 输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
# 示例 4：
# 输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
# 提示：
# 1 <= k <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/


# @lc code=start
import enum
import heapq


class Solution:
    from typing import List

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        l = sorted([[n, v] for n, v in d.items()])
        for i in range(len(l)):
            if l[i][1] > 0:
                v = l[i][1]
                for j in range(k):
                    if i + j >= len(l) or l[i + j][0] != l[i][0] + j or l[i + j][1] < v:
                        return False
                    l[i + j][1] = l[i + j][1] - v
        return True


# @lc code=end


func = Solution().isPossibleDivide
nums = [1, 2, 3, 3, 4, 4, 5, 6]
k = 4
print(func(nums, k))
# true

nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3
print(func(nums, k))
# true

nums = [3, 3, 2, 2, 1, 1]
k = 3
print(func(nums, k))
# true

nums = [1, 2, 3, 4]
k = 3
print(func(nums, k))
# false

nums = [1, 3, 5, 7]
k = 4
print(func(nums, k))
# false
