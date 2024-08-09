# @lc app=leetcode.cn id=372 lang=python3
# [372] 超级次方
# https://leetcode.cn/problems/super-pow/description/
# Medium (56.88%)
# Testcase Example:  '2\n[3]'
# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
# 示例 1：
# 输入：a = 2, b = [3]
# 输出：8
# 示例 2：
# 输入：a = 2, b = [1,0]
# 输出：1024
# 示例 3：
# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
# 示例 4：
# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198
# 提示：
# 1
# 1
# 0
# b 不含前导 0

# @lc code=start
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        self.base = 1337

        # (X * Y) % m = (X % m) * (Y % m) % m
        # sr(a, b) = pow(a, b[-1]) * pow(sr(a, b[:-1]), 10)

        def mypow1(a, k):
            if k == 0:
                return 1
            a %= self.base
            if k % 2 == 1:
                return a * mypow1(a, k - 1) % self.base
            sub = mypow1(a, k // 2)
            return (sub * sub) % self.base

        def sr(a, b):
            if not b:
                return 1
            return mypow1(a, b[-1]) * mypow1(sr(a, b[:-1]), 10) % self.base

        return sr(a, b)


# @lc code=end
# a = a = 2147483647
# b = [2, 0, 0]
# print(Solution().superPow(a, b))
