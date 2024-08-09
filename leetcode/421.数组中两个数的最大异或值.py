# @lc app=leetcode.cn id=421 lang=python3
# [421] 数组中两个数的最大异或值
# https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/description/
# Medium (59.75%)
# Testcase Example:  '[3,10,5,25,2,8]'
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 示例 1：
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
# 提示：
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1

# @lc code=start
class Solution:
    from typing import List
    def findMaximumXOR(self, nums: List[int]) -> int:
        pass
# @lc code=end


func = Solution().findMaximumXOR
nums = [3,10,5,25,2,8]
print(func(nums))
# 28

nums = [14,70,53,83,49,91,36,80,92,51,66,70]
print(func(nums))
# 127

