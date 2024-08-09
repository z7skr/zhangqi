# @lc app=leetcode.cn id=49 lang=python3
# [49] 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/description/
# Medium (67.80%)
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
# 提示：
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def brute_force(strs):
            res = {}
            for i, s in enumerate(strs):
                s = "".join(sorted(list(s)))
                res[s] = res.get(s, []) + [i]
            res = [[strs[i] for i in g] for g in res.values()]
            return res

        def hash_method(strs):
            def str2dict(s):
                x = [0] * 26
                for c in s:
                    x[ord(c) - ord("a")] += 1
                return tuple(x)

            res = {}
            for i, s in enumerate(strs):
                s = str2dict(s)
                res[s] = res.get(s, []) + [i]
            res = [[strs[i] for i in g] for g in res.values()]
            return res

        return hash_method(strs)


# @lc code=end
# print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
