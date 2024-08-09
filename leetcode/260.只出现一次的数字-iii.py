# @lc app=leetcode.cn id=260 lang=python3
# [260] 只出现一次的数字 III
# https://leetcode.cn/problems/single-number-iii/description/
# Medium (71.84%)
# Testcase Example:  '[1,2,1,3,2,5]'
# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。
# 示例 1：
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 示例 2：
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 示例 3：
# 输入：nums = [0,1]
# 输出：[1,0]
# 提示：
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次


# @lc code=start
from typing import List
from collections import Counter


class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        def best1():
            def isBitEq1(n, i):  # 检查右起的第i位是不是1
                return (n & (1 << i)) != 0

            def findFirstBitEq1(n):  # 查找右起第一个1是第几位
                for i in range(32):
                    if isBitEq1(n, i):
                        return i

            x, n = 0, len(nums)
            if n == 2:
                return nums
            for i in range(n):
                x ^= nums[i]  # x = a ^ b
            pos = findFirstBitEq1(x)  # xor=1表示在两个值
            # 根据在这一位的取值, 将数组分成两组, x1, x2必在不同组, 其他相同的数必在同一组
            x1, x2 = 0, 0
            for i in range(n):
                if isBitEq1(nums[i], pos):
                    x1 ^= nums[i]
                else:
                    x2 ^= nums[i]

            return [x1, x2]

        def best2():
            if len(nums) == 2:
                return nums
            x, x1, x2 = 0, 0, 0
            for i in range(len(nums)):
                x ^= nums[i]
            y = x - ((x - 1) & x)
            for i in range(len(nums)):
                if nums[i] & y > 0:
                    x1 ^= nums[i]
                else:
                    x2 ^= nums[i]
            return [x1, x2]

        def bt():
            return [k for k, v in Counter(nums).most_common()[-2:]]

        return best2()


# @lc code=end


func = Solution().singleNumber
nums = [1, 1, 2, 2, 4, 4, 3, 5]
print(func(nums))
# [3,5]

nums = [-1, 0]
print(func(nums))
# [-1,0]

nums = [0, 1]
print(func(nums))
# [1,0]
