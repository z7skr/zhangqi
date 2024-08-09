# @lc app=leetcode.cn id=645 lang=python3
# [645] 错误的集合
# https://leetcode.cn/problems/set-mismatch/description/
# Easy (39.08%)
# Testcase Example:  '[1,2,2,4]'
# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且
# 有一个数字重复 。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 示例 1：
# 输入：nums = [1,2,2,4]
# 输出：[2,3]
# 示例 2：
# 输入：nums = [1,1]
# 输出：[1,2]
# 提示：
# 2
# 1


# @lc code=start
class Solution:
    from typing import List

    def findErrorNums(self, nums: List[int]) -> List[int]:
        L = len(nums)

        def sort():
            nums.sort()
            for i in range(L - 1):
                if nums[i] == nums[i + 1]:
                    break
            return [nums[i], L * (L + 1) // 2 + nums[i] - sum(nums)]

        def count():
            lookup = [0] * L
            for num in nums:
                lookup[num - 1] += 1
            for i in range(L):
                if lookup[i] == 2:
                    dup = i + 1
                if lookup[i] == 0:
                    mis = i + 1
            return [dup, mis]

        def count2():
            lookup = [0] * L
            for num in nums:
                if lookup[num - 1] == 1:
                    return [num, L * (L + 1) // 2 + num - sum(nums)]
                lookup[num - 1] += 1
            return [0, 0]

        return count2()


# @lc code=end


func = Solution().findErrorNums
nums = [1, 2, 2, 4]
print(func(nums))
# [2,3]

nums = [1, 1]
print(func(nums))
# [1,2]
