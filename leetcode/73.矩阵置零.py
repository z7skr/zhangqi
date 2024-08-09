# @lc app=leetcode.cn id=73 lang=python3
# [73] 矩阵置零
# https://leetcode.cn/problems/set-matrix-zeroes/description/
# Medium (65.19%)
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 示例 1：
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 提示：
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 进阶：
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def f1(matrix):
            # - 先记录点, 再置零 O(mn)
            # ! 先记录行列, 再置零 O(m + n)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return
            m, n = len(matrix), len(matrix[0])
            rows, cols = [], []
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        rows.append(i)
                        cols.append(j)

            for i in rows:
                for j in range(n):
                    matrix[i][j] = 0

            for i in range(m):
                for j in cols:
                    matrix[i][j] = 0

        f1(matrix)


# @lc code=end
