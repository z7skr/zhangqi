# @lc app=leetcode.cn id=338 lang=python3
# [338] 比特位计数
# https://leetcode.cn/problems/counting-bits/description/
# Easy (78.70%)
# Testcase Example:  '2'
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans
# 作为答案。
# 示例 1：
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 示例 2：
# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 提示：
# 0 <= n <= 10^5
# 进阶：
# 很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
# 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）


# @lc code=start
class Solution:
    from typing import List

    def countBits(self, n: int) -> List[int]:
        def bf():
            def count(x):
                r = 0
                while x:
                    x = x & (x - 1)
                    r += 1
                return r

            return [count(i) for i in range(n + 1)]

        def recursive():
            res = [0, 1]
            while len(res) <= n + 1:
                next = [i + 1 for i in res]
                res += next
            return res[: n + 1]

        def best():
            res = [0] * (n + 1)
            gap = 1
            for i in range(1, n + 1):
                if i == gap * 2:
                    gap = i
                res[i] = res[i - gap] + 1
            return res

        return best()


# @lc code=end


func = Solution().countBits
n = 2
print(func(n))
# [0,1,1]

n = 5
print(func(n))
# [0,1,1,2,1,2]

n = 100
print(func(n))
# 0
# 1,
# 1, 2,
# 1, 2, 2, 3,
# 1, 2, 2, 3, 2, 3, 3, 4,
# 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
# 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
# 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3]
