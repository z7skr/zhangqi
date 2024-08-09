# @lc app=leetcode.cn id=1254 lang=python3
# [1254] 统计封闭岛屿的数目
# https://leetcode.cn/problems/number-of-closed-islands/description/
# Medium (64.00%)
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
# 请返回 封闭岛屿 的数目。
# 示例 1：
# 输入：grid =
# [
# [1,1,1,1,1,1,1,0],
# [1,0,0,0,0,1,1,0],
# [1,0,1,0,1,1,1,0],
# [1,0,0,0,0,1,0,1],
# [1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 示例 2：
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 示例 3：
# 输入：grid = [
# [1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# [1,1,1,1,1,1,1]
# ]
# 输出：2
# 提示：
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1


# @lc code=start
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        helper = [0, 0]  # 是否飞地, num

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 1:
                return
            grid[i][j] = 1
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
                if grid[i][j] == 0:
                    helper = [1, 0]  # 初始飞地
                    dfs(i, j)
                    res += helper[0]

        return res


# @lc code=end
grid = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
print(Solution().closedIsland(grid))
