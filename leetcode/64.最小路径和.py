# [64] 最小路径和
# https://leetcode.cn/problems/minimum-path-sum/description/
# Medium (70.56%)
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200


class Solution:
    from typing import List

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dp1():
            dp = [[0 for _ in range(n)] for _ in range(m)]
            dp[0][0] = grid[0][0]
            for i in range(1, m):
                dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, n):
                dp[0][j] = dp[0][j - 1] + grid[0][j]
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            return dp[-1][-1]

        def dp2():
            # 唯一不同是dp的起点（dp[j-1]）每次迭代i的时候不同
            dp = [0 for _ in range(n)]
            dp[0] = start = grid[0][0]
            for j in range(1, n):
                dp[j] = dp[j - 1] + grid[0][j]
            for i in range(1, m):
                start += grid[i][0]
                dp[0] = start
                for j in range(1, n):
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
            return dp[-1]

        return dp2()




func = Solution().minPathSum
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(func(grid))
# 7

grid = [[1, 2, 3], [4, 5, 6]]
print(func(grid))
# 12

