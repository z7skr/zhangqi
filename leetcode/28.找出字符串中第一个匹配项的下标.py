# @lc app=leetcode.cn id=28 lang=python3
# [28] 找出字符串中第一个匹配项的下标
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Easy (43.61%)
# Testcase Example:  '"sadbutsad"\n"sad"'
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 示例 1：
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
# 提示：
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def bf():
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i : i + len(needle)] == needle:
                    return i
            return -1

        # KMP 匹配算法，T 为文本串，p 为模式串
        def kmp(T: str, p: str) -> int:
            def generateNext(p: str):
                next = [0] * len(p)
                j = 0  # j 为前缀串的起始下标位置
                for i in range(1, len(p)):  # i 为后缀串的起始下标位置
                    while j > 0 and p[i] != p[j]:  # 匹配不成功, j 回退
                        j = next[j - 1]  # j 进行回退操作
                    if p[i] == p[j]:  # 匹配成功，继续匹配，此时 j 为前缀长度
                        j += 1
                    next[i] = j  # 记录前缀长度，更新 next[i], 结束本次循环, i += 1
                return next

            next = generateNext(p)
            j = 0  # j 为模式串中当前匹配的位置
            for i in range(len(T)):  # i 为文本串中当前匹配的位置
                while j > 0 and T[i] != p[j]:  # 匹配不成功, 将模式串回退
                    j = next[j - 1]
                if T[i] == p[j]:  # 匹配成功，继续匹配
                    j += 1
                if j == len(p):  # 当前模式串完全匹配成功，返回匹配开始位置
                    return i - j + 1
            return -1  # 匹配失败，返回 -1

        return kmp(haystack, needle)


# @lc code=end


func = Solution().strStr
haystack = "sadbutsad"
needle = "sad"
print(func(haystack, needle))
# 0

haystack = "leetcode"
needle = "leeto"
print(func(haystack, needle))
# -1
