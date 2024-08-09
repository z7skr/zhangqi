# @lc app=leetcode.cn id=1079 lang=python3
# [1079] 活字印刷
# https://leetcode.cn/problems/letter-tile-possibilities/description/
# Medium (79.05%)
# Testcase Example:  '"AAB"'
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 注意：本题中，每个活字字模只能使用一次。
# 示例 1：
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
# 输入："AAABBC"
# 输出：188
# 示例 3：
# 输入："V"
# 输出：1
# 提示：
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成


# @lc code=start


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(path, t):
            if path:
                res.add(path)  # 每一步都add
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i + 1 :])

        res = set()
        dfs("", tiles)
        return len(res)


# @lc code=end


func = Solution().numTilePossibilities

tiles = "A"
print(func(tiles))
# 1

tiles = "AA"
print(func(tiles))
# 2

tiles = "AB"
print(func(tiles))
# 4

tiles = "AAB"
print(func(tiles))
# 8

tiles = "ABC"
print(func(tiles))
# 15

tiles = "AAABBC"
print(func(tiles))
# 188
