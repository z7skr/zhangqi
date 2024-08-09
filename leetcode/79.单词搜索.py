# @lc app=leetcode.cn id=79 lang=python3
# [79] 单词搜索
# https://leetcode.cn/problems/word-search/description/
# Medium (46.89%)
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
# 示例 2：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
# 示例 3：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
# 提示：
# m == board.length
# n = board[i].length
# 1
# 1
# board 和 word 仅由大小写英文字母组成
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？


# @lc code=start
class Solution:
    from typing import List

    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.exist1(board, word)

    def exist1(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if (row, col) in visited or board[row][col] != word[i]:
                return False
            visited.add((row, col))
            res = (
                dfs(row, col + 1, i + 1)
                or dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            visited.remove((row, col))
            return res

        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[i]:
                return False
            tmp = board[row][col]
            board[row][col] = "#"
            res = (
                dfs(row, col + 1, i + 1)
                or dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            board[row][col] = tmp
            return res

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end


func = Solution().exist
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(func(board, word))
# true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(func(board, word))
# true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(func(board, word))
# false
