# @lc app=leetcode.cn id=417 lang=python3
# [417] 太平洋大西洋水流问题
# https://leetcode.cn/problems/pacific-atlantic-water-flow/description/
# Medium (56.35%)
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c)
# 上单元格 高于海平面的高度 。
# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。
# 返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动
# 既可流向太平洋也可流向大西洋 。
# 示例 1：
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# 示例 2：
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
# 提示：
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            if i == 0 or j == 0:
                flag[0] = 1
            if i == m - 1 or j == n - 1:
                flag[1] = 1
            for di, dj in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                if heights[ni][nj] <= heights[i][j]:
                    dfs(ni, nj)

        m, n = len(heights), len(heights[0])
        res = []
        for i in range(m):
            for j in range(n):
                flag = [0, 0]
                visited = set()
                dfs(i, j)
                if flag == [1, 1]:
                    res.append([i, j])

        return res


# @lc code=end
f = Solution().pacificAtlantic
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(f(heights))
heights = [[2, 1], [1, 2]]
print(f(heights))
