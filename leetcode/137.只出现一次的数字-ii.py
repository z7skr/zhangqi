# @lc app=leetcode.cn id=137 lang=python3
# [137] 只出现一次的数字 II
# https://leetcode.cn/problems/single-number-ii/description/
# Medium (72.28%)
# Testcase Example:  '[2,2,3,2]'
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
# 提示：
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次


# @lc code=start
class Solution:
    from typing import List

    def singleNumber(self, nums: List[int]) -> int:
        def bf():
            s = sum(nums)
            a = sum(set(nums))
            return s - (s - a) // 2 * 3

        def best():
            ones = 0
            twos = 0
            for num in nums:
                ones = (ones ^ num) & ~twos
                twos = (twos ^ num) & ~ones
            return ones

        return best()


# @lc code=end


func = Solution().singleNumber
nums = [2, 2, 3, 2]
print(func(nums))
# 3

nums = [0, 1, 0, 1, 0, 1, 99]
print(func(nums))
# 99
