# @lc app=leetcode.cn id=576 lang=python3
# [576] 出界的路径数
# https://leetcode.cn/problems/out-of-boundary-paths/description/
# Medium (47.03%)
# Testcase Example:  '2\n2\n2\n0\n0'
# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn]
# 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
# 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对
# 10^9 + 7 取余 后的结果。
# 示例 1：
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6
# 示例 2：
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12
# 提示：
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


# @lc code=start
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        memo = {}

        def move(i, j, curMove):
            if (i, j, curMove) in memo:
                return memo[(i, j, curMove)]
            if curMove < 0:
                return 0
            elif curMove >= 0 and (i == -1 or j == -1 or i == m or j == n):
                memo[(i, j, curMove)] = 1
            elif min(i, j, m - 1 - i, n - 1 - j) > curMove:
                memo[(i, j, curMove)] = 0
            else:
                memo[(i, j, curMove)] = (
                    move(i - 1, j, curMove - 1)
                    + move(i + 1, j, curMove - 1)
                    + move(i, j - 1, curMove - 1)
                    + move(i, j + 1, curMove - 1)
                )
            return memo[(i, j, curMove)]

        return move(startRow, startColumn, maxMove) % 1000000007


# @lc code=end


func = Solution().findPaths
m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(func(m, n, maxMove, startRow, startColumn))
# 6

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
print(func(m, n, maxMove, startRow, startColumn))
# 12

m = 7
n = 6
maxMove = 13
startRow = 0
startColumn = 2
print(func(m, n, maxMove, startRow, startColumn))
# 1659429
