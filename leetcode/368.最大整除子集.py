# @lc app=leetcode.cn id=368 lang=python3
# [368] 最大整除子集
# https://leetcode.cn/problems/largest-divisible-subset/description/
# Medium (45.92%)
# Testcase Example:  '[1,2,3]'
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
# 示例 2：
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
# 提示：
# nums 中的所有整数 互不相同


# @lc code=start
class Solution:
    from typing import List

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
        res = []
        cur = max(dp)
        idx = dp.index(cur)
        for _ in range(max(dp)):
            cur -= 1
            res.append(nums[idx])
            cands = [i for i in range(idx) if dp[i] == cur and nums[idx] % nums[i] == 0]
            if cands:
                idx = cands[0]

        return sorted(res)


# @lc code=end
func = Solution().largestDivisibleSubset
nums = [1, 2, 3]
print(func(nums))
# [1,2]

nums = [1, 2, 3, 4, 5, 7, 8, 12, 24, 25]
#  asdf[1, 2, 2, 3, 2, 2, 4,  4,  5,  3]
print(func(nums))
# [1,2,4,8]
