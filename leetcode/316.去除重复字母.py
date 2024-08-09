# @lc app=leetcode.cn id=316 lang=python3
# [316] 去除重复字母
# https://leetcode.cn/problems/remove-duplicate-letters/description/
# Medium (48.75%)
# Testcase Example:  '"bcabc"'
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 示例 1：
# 输入：s = "bcabc"
# 输出："abc"
# 示例 2：
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 提示：
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同

from collections import Counter


# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # last_occ = {}
        # stack = []
        # visited = set()

        # for i in range(len(s)):
        #     last_occ[s[i]] = i

        # for i in range(len(s)):

        #     if s[i] not in visited:
        #         while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
        #             visited.remove(stack.pop())

        #         stack.append(s[i])
        #         visited.add(s[i])

        # return "".join(stack)
        1


# @lc code=end
