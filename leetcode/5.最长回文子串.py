# @lc app=leetcode.cn id=5 lang=python3
# [5] 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/description/
# Medium (37.99%)
# Testcase Example:  '"babad"'
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search_from_inner_to_outer(s):
            # 从一个字母(or2)向外查询, 需要查询所有字母
            L = 1
            res = ""
            for i in range(len(s)):
                left = i
                rights = [i] if i < len(s) - 1 and s[i] != s[i + 1] else [i, i + 1]
                for right in rights:
                    l, r = left, right
                    while l >= 0 and r < len(s) and s[l] == s[r]:
                        l, r = l - 1, r + 1  # 1
                    if L < r - l + 1:
                        L = r - l + 1
                        res = s[l + 1 : r]
            return res

        def search_from_outer_to_inner(s):
            for L in reversed(range(1, len(s) + 1)):
                for left in range(len(s) - L + 1):
                    right = left + L - 1
                    l, r = left, right
                    f = 1
                    while l < r:
                        if s[l] != s[r]:
                            f = 0
                            break
                        l, r = l + 1, r - 1
                    if f:
                        return s[left : right + 1]
            return s

        return search_from_outer_to_inner(s)


# @lc code=end
func = Solution().longestPalindrome

s = "babad"
print(func(s))
# 输出："bab"
s = "cbbd"
print(func(s))
# 输出："bb"
s = "a"
print(func(s))
# 输出："a"
s = ""
print(func(s))
# 输出：""
