# @lc app=leetcode.cn id=54 lang=python3
# [54] 螺旋矩阵
# https://leetcode.cn/problems/spiral-matrix/description/
# Medium (50.18%)
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1
# -100

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def traverse_outter_circle(matrix, i1, j1, i2, j2):
            if i1 == i2:
                return matrix[i1][j1 : j2 + 1]
            if j1 == j2:
                return [matrix[i][j2] for i in range(i1, i2 + 1)]
            return (
                matrix[i1][j1:j2]  # 第一行除了最后一个点
                + [matrix[i][j2] for i in range(i1, i2)]  # 最后一列除了最后一个点
                + matrix[i2][j2:j1:-1]  # 最后一行逆序
                + [matrix[i][j1] for i in range(i2, i1, -1)]  # 第一列逆序
            )

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        # 右下角的点的坐标必大于左上角的点的坐标, 不用管超没超过中间
        while i <= m - 1 - i and j <= n - 1 - j:
            res.extend(traverse_outter_circle(matrix, i, j, m - 1 - i, n - 1 - j))
            i, j = i + 1, j + 1
        return res


# @lc code=end

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# print(Solution().spiralOrder(matrix))

x = [1, 2, 3, 4, 5]
