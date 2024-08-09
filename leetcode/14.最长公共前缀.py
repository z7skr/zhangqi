# @lc app=leetcode.cn id=14 lang=python3
# [14] 最长公共前缀
# https://leetcode.cn/problems/longest-common-prefix/description/
# Easy (43.71%)
# Testcase Example:  '["flower","flow","flight"]'
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 提示：
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成


# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefix_dc(strs)

    def commonPrefix(self, s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return s1[:i]

    def longestCommonPrefix_dc(self, strs: List[str]):  # 分治
        L = len(strs)
        if L == 1:
            return strs[0]
        else:
            left = self.longestCommonPrefix_dc(strs[: L // 2])
            right = self.longestCommonPrefix_dc(strs[L // 2 :])
            return self.commonPrefix(left, right)

    def longestCommonPrefix_bf1(self, strs: List[str]) -> str:
        r = strs[0]
        for i in range(1, len(strs)):
            c = strs[i]
            r = self.commonPrefix(r, c)
        return r

    def longestCommonPrefix_bf2(self, strs: List[str]) -> str:
        L = len(strs[0])
        for s in strs[1:]:
            L = min(L, len(s))
        res = []
        for i in range(L):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return "".join(res)
            res.append(c)
        return "".join(res)


# @lc code=end
func = Solution().longestCommonPrefix
strs = ["flower", "flow", "flight"]
print(func(strs))
# 输出："fl"
strs = ["dog", "racecar", "car"]
print(func(strs))
# 输出：""
strs = [""]
print(func(strs))
# 输出：""
strs = ["ab", "a"]
print(func(strs))
# 输出："a"
