# @lc app=leetcode.cn id=673 lang=python3
# [673] 最长递增子序列的个数
# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description/
# Medium (44.79%)
# Testcase Example:  '[1,3,5,4,7]'
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
# 注意 这个数列必须是 严格 递增的。
# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 提示:
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6


# @lc code=start
class Solution:
    from typing import List

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        m, dp, cnt = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 换新
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]  # 增加
            m = max(m, dp[i])
        return sum(c for l, c in zip(dp, cnt) if l == m)


# @lc code=end


func = Solution().findNumberOfLIS

nums = [1, 3, 5, 4, 7]
print(func(nums))
# 输出: 2

nums = [2, 2, 2, 2, 2, 3]
print(func(nums))
# 输出: 5

nums = [2, 2, 2, 2, 2]
print(func(nums))
# 输出: 5
