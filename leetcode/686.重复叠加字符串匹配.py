# @lc app=leetcode.cn id=686 lang=python3
# [686] 重复叠加字符串匹配
# https://leetcode.cn/problems/repeated-string-match/description/
# Medium (39.70%)
# Testcase Example:  '"abcd"\n"cdabcdab"'
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
# 示例 1：
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
# 示例 2：
# 输入：a = "a", b = "aa"
# 输出：2
# 示例 3：
# 输入：a = "a", b = "a"
# 输出：1
# 示例 4：
# 输入：a = "abc", b = "wxyz"
# 输出：-1
# 提示：
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a 和 b 由小写英文字母组成


# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def f1():
            la, lb = len(a), len(b)
            start = lb // la if lb % la == 0 else lb // la + 1
            for i in range(start, start + 2):
                if b in a * i:
                    return i
            return -1

        def f2():
            if not set(b).issubset(set(a)):
                return -1
            for i in range(1, int(len(b) / len(a)) + 3):
                if b in a * i:
                    return i
            return -1

        return f2()


# @lc code=end


func = Solution().repeatedStringMatch
a = "abcd"
b = "cdabcdab"
print(func(a, b))
# 3

a = "a"
b = "aa"
print(func(a, b))
# 2

a = "a"
b = "a"
print(func(a, b))
# 1

a = "abc"
b = "wxyz"
print(func(a, b))
# -1
