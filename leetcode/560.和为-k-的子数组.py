# @lc app=leetcode.cn id=560 lang=python3
# [560] 和为 K 的子数组
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
# Medium (44.39%)
# Testcase Example:  '[1,1,1]\n2'
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2
# 提示：
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

from typing import List


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力解法 TLE
        def traverse(nums, k):
            res = 0
            for i in range(len(nums)):
                tmp = 0
                for j in range(i, len(nums)):
                    tmp += nums[j]
                    if tmp == k:
                        res += 1
            return res

        def presum(nums, k):
            res = 0
            ps = {0: 1}  # 某个 presum 的个数
            cs = 0  # cur sum
            for i, n in enumerate(nums):
                cs += n
                res += ps.get(cs - k, 0)
                ps[cs] = ps.get(cs, 0) + 1
            return res

        return presum(nums, k)


# @lc code=end
