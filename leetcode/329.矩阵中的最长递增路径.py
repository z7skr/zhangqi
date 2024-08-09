# @lc app=leetcode.cn id=329 lang=python3
# [329] 矩阵中的最长递增路径
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
# Hard (52.09%)
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
# 示例 1：
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4
# 解释：最长递增路径为 [1, 2, 6, 9]。
# 示例 2：
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 示例 3：
# 输入：matrix = [[1]]
# 输出：1
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1
# 0


# @lc code=start
class Solution:
    from typing import List

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def compute(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = 1
            if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                res = max(res, 1 + compute(i - 1, j))
            if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                res = max(res, 1 + compute(i, j - 1))
            if i < m - 1 and matrix[i][j] < matrix[i + 1][j]:
                res = max(res, 1 + compute(i + 1, j))
            if j < n - 1 and matrix[i][j] < matrix[i][j + 1]:
                res = max(res, 1 + compute(i, j + 1))
            memo[(i, j)] = res
            return memo[(i, j)]

        for i in range(m):
            for j in range(n):
                compute(i, j)

        return max(list(memo.values()))


# @lc code=end


func = Solution().longestIncreasingPath
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(func(matrix))
# 4

matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(func(matrix))
# 4

matrix = [[1]]
print(func(matrix))
# 1
