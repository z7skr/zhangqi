# @lc app=leetcode.cn id=557 lang=python3
# [557] 反转字符串中的单词 III
# https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
# Easy (73.66%)
# Testcase Example:  `"Let's take LeetCode contest"`
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 示例 1：
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 示例 2:
# 输入： s = "Mr Ding"
# 输出："rM gniD"
# 提示：
# 1 <= s.length <= 5 * 10^4
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        L = len(s)
        ls = list(s)
        i = 0
        while i < L:
            j = i
            while j + 1 < L and ls[j + 1] != " ":
                j += 1
            start = j + 2
            while i < j:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            i = start
        return "".join(ls)


# @lc code=end


func = Solution().reverseWords
s = "Let's take LeetCode contest"
print(func(s))
# "s'teL ekat edoCteeL tsetnoc"

s = "Mr Ding"
print(func(s))
# "rM gniD"
