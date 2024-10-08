# @lc app=leetcode.cn id=51 lang=python3
# [51] N 皇后
# https://leetcode.cn/problems/n-queens/description/
# Hard (74.09%)
# Testcase Example:  '4'
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例 1：
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
# 输入：n = 1
# 输出：[["Q"]]
# 提示：
# 1 <= n <= 9


# @lc code=start
class Solution:
    from typing import List

    def solveNQueens(self, n: int) -> List[List[str]]:
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
                res.append(["".join(line) for line in board])
                return
            for j in range(n):
                if cheak(i, j):
                    board[i][j] = "Q"
                    dfs(i + 1)
                    board[i][j] = "."

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        dfs(0)
        return res


# @lc code=end


func = Solution().solveNQueens
n = 4
print(func(n))
# [[".Q..",
#   "...Q",
#   "Q...",
#   "..Q."],
#  ["..Q.",
#   "Q...",
#   "...Q",
#   ".Q.."]]

n = 1
print(func(n))
# [["Q"]]
