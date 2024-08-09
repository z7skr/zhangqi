# @lc app=leetcode.cn id=773 lang=python3
# [773] 滑动谜题
# https://leetcode.cn/problems/sliding-puzzle/description/
# Hard (70.16%)
# Testcase Example:  '[[1,2,3],[4,0,5]]'
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0
# 与一个相邻的数字（上下左右）进行交换.
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 示例 1：
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 示例 2:
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 示例 3:
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
# 提示：
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# board[i][j] 中每个值都 不同
# @lc code=start
from copy import deepcopy
from typing import List
from collections import deque

from pyparsing import C


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # x = [[1,2,3],[4,0,5]]
        m, n = len(board), len(board[0])
        q = deque([board])
        visited = []
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                visited.append(c)
                if c == [[1, 2, 3], [4, 5, 0]]:
                    return res
                if 0 in c[0]:
                    i, j = 0, c[0].index(0)
                else:
                    i, j = 1, c[1].index(0)
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        continue
                    b = deepcopy(c)
                    b[i][j], b[ni][nj] = b[ni][nj], b[i][j]
                    # print(c, i, j, ni, nj, b)
                    if b not in visited and b not in q:
                        q.append(b)

            res += 1
        return -1


# @lc code=end

f = Solution().slidingPuzzle

board = [[1, 2, 3], [4, 0, 5]]
# 输出：1
print(f(board))
board = [[1, 2, 3], [5, 4, 0]]
# 输出：-1
print(f(board))
board = [[4, 1, 2], [5, 0, 3]]
# 输出：5
print(f(board))
