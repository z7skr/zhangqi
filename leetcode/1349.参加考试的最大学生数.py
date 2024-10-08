# @lc app=leetcode.cn id=1349 lang=python3
# [1349] 参加考试的最大学生数
# https://leetcode.cn/problems/maximum-students-taking-exam/description/
# Hard (63.84%)
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的
# 最大 学生人数。
# 学生必须坐在状况良好的座位上。
# 示例 1：
# 输入：seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
# 示例 2：
# 输入：seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 示例 3：
# 输入：seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
# 提示：
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8


# @lc code=start


class Solution:
    from typing import List

    def maxStudents(self, seats: List[List[str]]) -> int:

        m, n = len(seats), len(seats[0])

        def dfs():
            def dfs(row, col):
                nonlocal ans, res
                if row == m:
                    if res > ans:
                        ans = res
                        print(ans)
                        for s in seats:
                            print(s)
                        print()
                elif col == n:
                    dfs(row + 1, 0)
                elif seats[row][col] == "#":
                    dfs(row, col + 1)
                elif rest[row * n + col] + res < ans:
                    dfs(row, col + 1)
                elif (
                    row > 0
                    and (
                        col > 0
                        and seats[row - 1][col - 1] == "!"
                        or col < n - 1
                        and seats[row - 1][col + 1] == "!"
                    )
                    or col > 0
                    and seats[row][col - 1] == "!"
                ):
                    dfs(row, col + 1)
                else:
                    seats[row][col] = "!"
                    res += 1
                    dfs(row, col + 1)
                    res -= 1
                    seats[row][col] = "."
                    dfs(row, col + 1)

            ans, res = 0, 0
            rest = [0] * (m * n)
            cur = 0
            for i in reversed(range(m)):
                for j in reversed(range(n)):
                    if seats[i][j] == ".":
                        cur += 1
                    rest[i * n + j] = cur

            dfs(0, 0)
            return ans

        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if seats[i][j] == ".":
                    cols[j] += 1

        for j in range(n):

        return dfs()


# @lc code=end


func = Solution().maxStudents
seats = [
    ["#", ".", "#", "#", ".", "#"],
    [".", "#", "#", "#", "#", "."],
    ["#", ".", "#", "#", ".", "#"],
]
# print(func(seats))
# 4

seats = [[".", "#"], ["#", "#"], ["#", "."], ["#", "#"], [".", "#"]]
# print(func(seats))
# 3

seats = [
    ["#", ".", ".", ".", "#"],
    [".", "#", ".", "#", "."],
    [".", ".", "#", ".", "."],
    [".", "#", ".", "#", "."],
    ["#", ".", ".", ".", "#"],
]
# print(func(seats))
# 10

seats = [
    [".", ".", ".", ".", "#", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", "#", "."],
]
print(func(seats))
# 31
