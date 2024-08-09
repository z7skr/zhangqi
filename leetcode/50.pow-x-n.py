# @lc app=leetcode.cn id=50 lang=python3
# [50] Pow(x, n)
# https://leetcode.cn/problems/powx-n/description/
# Medium (38.25%)
# Testcase Example:  '2.00000\n10'
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，x^n^ ）。
# 示例 1：
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
# 提示：
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -10^4 <= x^n <= 10^4


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif x == 0:
            return 0
        t = self.myPow(x, n >> 1)
        return t * t * self.myPow(x, n & 1)


# @lc code=end


func = Solution().myPow
x = 2.00000
n = 10
print(func(x, n))
# 1024.00000

x = 2.10000
n = 3
print(func(x, n))
# 9.26100

x = 2.00000
n = -2
print(func(x, n))
# 0.25000
