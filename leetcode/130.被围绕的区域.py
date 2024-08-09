# @lc app=leetcode.cn id=130 lang=python3
# [130] 被围绕的区域
# https://leetcode.cn/problems/surrounded-regions/description/
# Medium (46.40%)
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X'
# 填充。
# 示例 1：
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：
# 输入：board = [["X"]]
# 输出：[["X"]]
# 提示：
# m == board.length
# n == board[i].length
# 1
# board[i][j] 为 'X' 或 'O'


# @lc code=start
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anjthing, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        need_change = [0]

        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return
            if (i, j) in visited or board[i][j] == "X":
                return
            visited.add((i, j))
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                need_change[0] = 0
            for di, dj in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                dfs(i + di, j + dj)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    need_change[0] = 1
                    visited = set()
                    dfs(i, j)
                    if need_change[0] == 1:
                        for x, y in visited:
                            board[x][y] = "X"
        for i in range(m):
            print("".join(board[i]))


# @lc code=end
f = Solution().solve
board = [
    ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],  # 0
    ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],  # 1
    ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],  # 2
    ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],  # 3
    ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],  # 4
    ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],  # 5
    ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],  # 6
    ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],  # 7
    ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],  # 8
    ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],  # 9
]
f(board)
board = [["X"]]
f(board)
