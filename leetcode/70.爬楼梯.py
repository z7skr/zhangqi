# @lc app=leetcode.cn id=70 lang=python3
# [70] 爬楼梯
# https://leetcode.cn/problems/climbing-stairs/description/
# Easy (54.51%)
# Testcase Example:  '2'
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
# 提示：
# 1 <= n <= 45


# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def recursive(n):
            if n in memo:
                return memo[n]
            memo[n] = recursive(n - 1) + recursive(n - 2)
            return memo[n]

        return recursive(n)


# @lc code=end


func = Solution().climbStairs
n = 2
print(func(n))
# 2

n = 3
print(func(n))
# 3

n = 5
print(func(n))
# 8
