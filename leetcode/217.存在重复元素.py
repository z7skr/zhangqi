# @lc app=leetcode.cn id=217 lang=python3
# [217] 存在重复元素
# https://leetcode.cn/problems/contains-duplicate/description/
# Easy (55.07%)
# Testcase Example:  '[1,2,3,1]'
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 示例 1：
# 输入：nums = [1,2,3,1]
# 输出：true
# 示例 2：
# 输入：nums = [1,2,3,4]
# 输出：false
# 示例 3：
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true
# 提示：
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def f0(nums):
            # 79%, 45%
            return len(nums) != len(set(nums))
        def f1(nums):
            # 16%, 99%
            nums.sort()
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    return True
            return False
        def f2(nums):
            # 95%， 50%
            sets = set()
            for n in nums:
                if n in sets:
                    return True
                sets.add(n)
            return False
        return f2(nums)
# @lc code=end
