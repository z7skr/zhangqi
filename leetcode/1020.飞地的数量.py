# @lc app=leetcode.cn id=1020 lang=python3
# [1020] 飞地的数量
# https://leetcode.cn/problems/number-of-enclaves/description/
# Medium (61.86%)
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
# 示例 1：
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 示例 2：
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        helper = [0, 0]  # 是否飞地, num

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            helper[1] += 1
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                helper[0] = 0  # 不是飞地
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    helper = [1, 0]  # 初始飞地
                    dfs(i, j)
                    res += helper[0] * helper[1]

        return res


# @lc code=end
grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(Solution().numEnclaves(grid))
grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
print(Solution().numEnclaves(grid))
