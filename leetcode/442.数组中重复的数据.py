# @lc app=leetcode.cn id=442 lang=python3
# [442] 数组中重复的数据
# https://leetcode.cn/problems/find-all-duplicates-in-an-array/description/
# Medium (75.07%)
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次
# 的整数，并以数组形式返回。
# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
# 示例 1：
# 输入：nums = [1,2,2,3,3,4,7,8]
# 输出：[2,3]
# 示例 2：
# 输入：nums = [1,1,2]
# 输出：[1]
# 示例 3：
# 输入：nums = [1]
# 输出：[]
# 提示：
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# nums 中的每个元素出现 一次 或 两次

# @lc code=start
from collections import Counter
class Solution:
    from typing import List
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def f1():
            return [k for k, v in Counter(nums).items() if v == 2]
        def f2():
            # 遍历数组, 因为每个数都在 [1, n] 之间所以 num-1 是合法的 idx,
            # 把 nums[num-1] 设为负数, 如果第二次遇到 nums[num-1] 是负数的说明 num 重复了
            res = []
            i = 0
            for i in range(len(nums)):
                idx = abs(nums[i]) - 1
                if nums[idx] < 0:
                    res.append(abs(nums[i]))
                else:
                    nums[idx] = -nums[idx]
            return res
        return f2()

# @lc code=end


func = Solution().findDuplicates
nums = [4,3,2,7,8,2,3,1]
print(func(nums))
# [2,3]

nums = [1,1,2]
print(func(nums))
# [1]

nums = [1]
print(func(nums))
# []

