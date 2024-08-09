# @lc app=leetcode.cn id=45 lang=python3
# [45] 跳跃游戏 II
# https://leetcode.cn/problems/jump-game-ii/description/
# Medium (44.42%)
# Testcase Example:  '[2,3,1,1,4]'
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2
# 提示:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]


# @lc code=start
class Solution:
    from typing import List

    def jump(self, nums: List[int]) -> int:
        def dp():
            dp = [len(nums)] * len(nums)
            dp[0] = 0
            for i in range(len(nums)):
                for j in range(i + 1):
                    if j + nums[j] >= i:
                        dp[i] = min(dp[i], 1 + dp[j])
            return dp[-1]

        def bfs():
            n, start, end, step = len(nums), 0, 0, 0
            while end < n - 1:
                step += 1
                maxend = end + 1  # 最远位置至少+1
                for i in range(start, end + 1):
                    maxend = max(maxend, i + nums[i])
                    if maxend >= n - 1:
                        return step
                start, end = end + 1, maxend
            return step

        return bfs()


# @lc code=end


func = Solution().jump
nums = [2, 3, 1, 1, 4]
print(func(nums))
#  2

nums = [2, 3, 0, 1, 4]
print(func(nums))
#  2

nums = [0]
print(func(nums))
#  0

nums = [1, 1]
print(func(nums))
#  0
