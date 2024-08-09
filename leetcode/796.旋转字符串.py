# @lc app=leetcode.cn id=796 lang=python3
# [796] 旋转字符串
# https://leetcode.cn/problems/rotate-string/description/
# Easy (63.62%)
# Testcase Example:  '"abcde"\n"cdeab"'
# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。
# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
# 示例 1:
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
# 示例 2:
# 输入: s = "abcde", goal = "abced"
# 输出: false
# 1 <= s.length, goal.length <= 100
# s 和 goal 由小写英文字母组成


# aba aab
# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def f1():
            for i in range(len(s)):
                if s[i] == goal[0]:
                    if s[i:] + s[:i] == goal:
                        return True
            return False

        def f2():
            return len(s) == len(goal) and s in goal + goal

        return f2()


# @lc code=end


func = Solution().rotateString
s = "abcde"
goal = "cdeab"
print(func(s, goal))
#  true

s = "abcde"
goal = "abced"
print(func(s, goal))
#  false
