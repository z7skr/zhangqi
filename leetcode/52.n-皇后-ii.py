# @lc app=leetcode.cn id=52 lang=python3
# [52] N 皇后 II
# https://leetcode.cn/problems/n-queens-ii/description/
# Hard (82.30%)
# Testcase Example:  '4'
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 示例 1：
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
# 输入：n = 1
# 输出：1
# 提示：
# 1 <= n <= 9


# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def cheak(i, j):
            for d in range(1, i + 1):
                if board[i - d][j] == "Q":
                    return False
                if j - d >= 0 and board[i - d][j - d] == "Q":
                    return False
                if j + d < n and board[i - d][j + d] == "Q":
                    return False
            return True

        def dfs(i):
            if i == n:
                res[0] += 1
            for j in range(n):
                if cheak(i, j):
                    board[i][j] = "Q"
                    dfs(i + 1)
                    board[i][j] = "."

        res = [0]
        board = [["." for _ in range(n)] for _ in range(n)]
        dfs(0)
        return res[0]
        return [1, 0, 0, 2, 10, 4, 40, 92, 352][n - 1]


# @lc code=end


func = Solution().totalNQueens
n = 4
print(func(n))
# 2

n = 1
print(func(n))
# 1
