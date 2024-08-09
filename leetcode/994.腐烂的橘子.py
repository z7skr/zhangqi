# @lc app=leetcode.cn id=994 lang=python3
# [994] 腐烂的橘子
# https://leetcode.cn/problems/rotting-oranges/description/
# Medium (52.36%)
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
# 示例 1：
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 示例 2：
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
# 示例 3：
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] 仅为 0、1 或 2


# @lc code=start
from collections import deque


class Solution:
    from typing import List

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        res = -1
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                if i + 1 < m and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    q.append((i + 1, j))
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    q.append((i - 1, j))
                if j + 1 < n and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    q.append((i, j + 1))
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    q.append((i, j - 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        if sum(sum(line) for line in grid) == 0:
            return 0

        return res


# @lc code=end


func = Solution().orangesRotting
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

# 2 1 1 | 2 2 1 | 2 2 2 | 2 2 2 | 2 2 2 |
# 1 1 0 | 2 1 0 | 2 2 0 | 2 2 0 | 2 2 0 |
# 0 1 1 | 0 1 1 | 0 1 1 | 0 2 1 | 0 2 2 |
print(func(grid))
# 4

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(func(grid))
# -1

grid = [[0, 2]]
print(func(grid))
# 0
