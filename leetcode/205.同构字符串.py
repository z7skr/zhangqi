# @lc app=leetcode.cn id=205 lang=python3
# [205] 同构字符串
# https://leetcode.cn/problems/isomorphic-strings/description/
# Easy (49.34%)
# Testcase Example:  '"egg"\n"add"'
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
# 示例 1:
# 输入：s = "egg", t = "add"
# 输出：true
# 示例 2：
# 输入：s = "foo", t = "bar"
# 输出：false
# 示例 3：
# 输入：s = "paper", t = "title"
# 输出：true
# 提示：
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成

# @lc code=start
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(s):
            d = {}
            res = []
            ch = 'a'
            for c in s:
                if c not in d:
                    d[c] = ch
                    ch = chr(ord(ch) + 1)
                res.append(d[c])
            return ''.join(res)
        return transform(s) == transform(t)
# @lc code=end


func = Solution().isIsomorphic
s = "egg"
t = "add"
print(func(s, t))
# true

s = "foo"
t = "bar"
print(func(s, t))
# false

s = "paper"
t = "title"
print(func(s, t))
# true

