# @lc app=leetcode.cn id=454 lang=python3
# [454] 四数相加 II
# https://leetcode.cn/problems/4sum-ii/description/
# Medium (64.40%)
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l)
# 能满足：
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 示例 1：
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 示例 2：
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
# 提示：
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28

# @lc code=start
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def f1():
            from collections import Counter
            c1 = Counter([a + b for a in nums1 for b in nums2])
            c2 = Counter([a + b for a in nums3 for b in nums4])
            return sum([c1[k] * c2[-k] for k in c1 if -k in c2])
        def f2():
            from collections import Counter
            c = Counter([a + b for a in nums3 for b in nums4])
            return sum([c.get(-a - b, 0) for a in nums1 for b in nums2])
        return f2()
# @lc code=end


func = Solution().fourSumCount
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(func(nums1, nums2, nums3, nums4))
# 2
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(func(nums1, nums2, nums3, nums4))
# 1
nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]
print(func(nums1, nums2, nums3, nums4))
# 6
