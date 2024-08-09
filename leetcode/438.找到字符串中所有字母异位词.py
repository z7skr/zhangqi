# @lc app=leetcode.cn id=438 lang=python3
# [438] 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
# Medium (54.00%)
# Testcase Example:  '"cbaebabacd"\n"abc"'
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 提示:
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        need = {}
        for c in p:
            need[c] = need[c] + 1 if c in need else 1
        window = {}
        valid = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)
                c = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res


# @lc code=end
