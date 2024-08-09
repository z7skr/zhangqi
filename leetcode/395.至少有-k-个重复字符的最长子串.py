# @lc app=leetcode.cn id=395 lang=python3
# [395] 至少有 K 个重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/
# Medium (52.59%)
# Testcase Example:  '"aaabb"\n3'
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
# 如果不存在这样的子字符串，则返回 0。
# 示例 1：
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2：
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
# 提示：
# 1 <= s.length <= 10^4
# s 仅由小写英文字母组成
# 1 <= k <= 10^5
import collections


# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 分治
        # 73%, 35%
        def f1(s, k):
            # 定义: 返回 s 的子串中每一字符出现次数都不少于 k 的最长子串长度
            # 计数
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            # 找出不可能包含的字母, 切割
            for i in range(26):
                if counts[i] > 0 and counts[i] < k:
                    c = chr(i + ord("a"))
                    res = 0
                    for ss in s.split(c):
                        if ss:
                            res = max(res, f1(ss, k))
                    return res
            # 没找到说明全都不小于k，直接返回len(s)
            return len(s)

        # 分治优化一下
        def f2(s, k):
            cnt = collections.Counter(s)
            start = 0  # 标记下一个子串的起点，同时也是判断是否切分s的标记
            res = 0
            for i, c in enumerate(s):
                if cnt[c] < k:
                    res = max(res, f2(s[start:i], k))
                    start = i + 1
            return len(s) if start == 0 else max(res, f2(s[start:], k))

        return f2(s, k)


# @lc code=end
