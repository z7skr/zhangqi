# @lc app=leetcode.cn id=1143 lang=python3
# [1143] 最长公共子序列
# https://leetcode.cn/problems/longest-common-subsequence/description/
# Medium (65.03%)
# Testcase Example:  '"abcde"\n"ace"'
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列
# 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
# 提示：
# 1
# text1 和 text2 仅由小写英文字符组成。


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = len(text1), len(text2)
        dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[a][b]


# @lc code=end

func = Solution().longestCommonSubsequence

text1 = "abcde"
text2 = "ace"
print(func(text1, text2))
# 输出：3
text1 = "abc"
text2 = "abc"
print(func(text1, text2))
# 输出：3
text1 = "abc"
text2 = "def"
print(func(text1, text2))
# 输出：0
