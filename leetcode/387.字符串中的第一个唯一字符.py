# @lc app=leetcode.cn id=387 lang=python3
# [387] 字符串中的第一个唯一字符
# https://leetcode.cn/problems/first-unique-character-in-a-string/description/
# Easy (56.37%)
# Testcase Example:  '"leetcode"'
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 示例 1：
# 输入: s = "leetcode"
# 输出: 0
# 示例 2:
# 输入: s = "loveleetcode"
# 输出: 2
# 示例 3:
# 输入: s = "aabb"
# 输出: -1
# 提示:
# 1 <= s.length <= 10^5
# s 只包含小写字母


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        def f1():
            d = {}
            for c in s:
                d[c] = d.get(c, 0) + 1
            for i, c in enumerate(s):
                if d[c] == 1:
                    return i
            return -1
        def f2():
            visited = set()
            for i, c in enumerate(s):
                if c not in visited and c not in s[i+1:]:
                    return i
                visited.add(c)
            return -1
        return f2()


# @lc code=end


func = Solution().firstUniqChar
s = "leetcode"
print(func(s))
#  0

s = "loveleetcode"
print(func(s))
#  2

s = "aabb"
print(func(s))
#  -1
