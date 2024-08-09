# @lc app=leetcode.cn id=779 lang=python3
# [779] 第K个语法符号
# https://leetcode.cn/problems/k-th-symbol-in-grammar/description/
# Medium (49.89%)
# Testcase Example:  '1\n1'
# 我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个
# 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
# 给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）
# 示例 1:
# 输入: n = 1, k = 1
# 输出: 0
# 解释: 第一行：0
# 示例 2:
# 输入: n = 2, k = 1
# 输出: 0
# 解释:
# 第一行: 0
# 第二行: 01
# 示例 3:
# 输入: n = 2, k = 2
# 输出: 1
# 解释:
# 第一行: 0
# 第二行: 01
# 提示:
# 1 <= n <= 30
# 1 <= k <= 2^n - 1


# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 0 if k == 1 else 1
        h = 1 << (n - 2)
        if k > h:
            return 1 - self.kthGrammar(n - 1, k - h)
        return self.kthGrammar(n - 1, k)


# @lc code=end
# 1 -> 2  -> 3    -> 4        -> 5
# 0 -> 01 -> 0110 -> 01101001 -> 0110100110010110
func = Solution().kthGrammar
n = 1
k = 1
print(func(n, k))
#  0

n = 2
k = 1
print(func(n, k))
#  0

n = 2
k = 2
print(func(n, k))
#  1

n = 3
k = 4
print(func(n, k))
#  0

n = 4
k = 5
print(func(n, k))
#  1
