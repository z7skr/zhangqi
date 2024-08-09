# @lc app=leetcode.cn id=459 lang=python3
# [459] 重复的子字符串
# https://leetcode.cn/problems/repeated-substring-pattern/description/
# Easy (51.41%)
# Testcase Example:  '"abab"'
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
# 示例 1:
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
# 示例 2:
# 输入: s = "aba"
# 输出: false
# 示例 3:
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
# 提示：
# 1 <= s.length <= 10^4
# s 由小写英文字母组成


# @lc code=start
import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def f1():
            length = len(s)
            if length == 1:
                return False
            for n in reversed(range(1, length + 1)):
                if length % n != 0:
                    continue
                k = length // n
                if n == 1:
                    return len(set(list(s))) == 1
                f = 1
                for i in range(0, length, k):
                    if s[:k] != s[i : i + k]:
                        f = 0
                        break
                if f == 1 and n > 1:
                    return True
            return False

        def f2():
            return re.match(r"^(.*)\1+$", s) is not None

        def f3():
            return s in s[1:] + s[:-1]

        return f3()


# @lc code=end


func = Solution().repeatedSubstringPattern
s = "abab"  # bababa
print(func(s))
#  true

s = "aba"
print(func(s))
#  false

s = "abcabcabcabc"
print(func(s))
#  true

s = "bb"
print(func(s))
#  true

s = "ababba"  # babbaababb
print(func(s))
#  false
