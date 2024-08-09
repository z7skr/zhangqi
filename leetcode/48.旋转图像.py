# @lc app=leetcode.cn id=48 lang=python3
# [48] 旋转图像
# https://leetcode.cn/problems/rotate-image/description/
# Medium (75.52%)
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
# 示例 2：
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# n=4, n-1=3
# 1: 0, 1 (i, j)
# 1: 1, 3 (j, n-1-i)
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 提示：
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0:
            return
        n = len(matrix)
        #
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                i1, j1 = i, j
                i2, j2 = j1, n - 1 - i1
                i3, j3 = n - 1 - i1, n - 1 - j1
                i4, j4 = n - 1 - i2, n - 1 - j2
                matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
                matrix[i1][j1], matrix[i3][j3] = matrix[i3][j3], matrix[i1][j1]
                matrix[i1][j1], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1]


# @lc code=end
