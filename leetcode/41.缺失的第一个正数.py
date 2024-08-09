# @lc app=leetcode.cn id=41 lang=python3
# [41] 缺失的第一个正数
# https://leetcode.cn/problems/first-missing-positive/description/
# Hard (43.84%)
# Testcase Example:  '[1,2,0]'
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 示例 1：
# 输入：nums = [1,2,0]
# 输出：3
# 示例 2：
# 输入：nums = [3,4,-1,1]
# 输出：2
# 示例 3：
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 提示：
# 1
# -2^31

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def labeling(nums):
            n = len(nums)
            # 把不在 [1, n] 范围的都替换成 n + 1, 如果数组有 n + 1 答案肯定不是 n + 1
            for i in range(n):
                if nums[i] < 1 or nums[i] > n:
                    nums[i] = n + 1
            # 对每个值在 [1, n] 内的数，在 v-1 的位置打标签, 已经打过的重复打
            for i in range(n):
                pos = abs(nums[i]) - 1
                if pos < n:  # abs(nums[i]) - 1 ∈ [0, n)
                    nums[pos] = -abs(nums[pos])
            for i in range(n):
                if nums[i] > 0:
                    return i + 1
            return n + 1

        def switch(nums):
            n = len(nums)
            for i in range(n):
                while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1
            return n + 1

        return switch(nums)


# @lc code=end
print(Solution().firstMissingPositive([3, 4, -1, 1]))
