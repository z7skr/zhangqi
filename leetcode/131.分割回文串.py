# @lc app=leetcode.cn id=131 lang=python3
# [131] 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning/description/
# Medium (73.50%)
# Testcase Example:  '"aab"'
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 示例 1：
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
# 输入：s = "a"
# 输出：[["a"]]
# 提示：
# 1 <= s.length <= 16
# s 仅由小写英文字母组成


# @lc code=start
class Solution:
    from typing import List

    def partition(self, s: str) -> List[List[str]]:
        def dfs(i, path):
            if i == len(s):
                res.append(path)
                return
            dfs(i + 1, path + [s[i]])  # 单个字符一定是回文串
            # 看以 s[i] 开头的是不是回文串
            start = i + 1  # 起点从下一个开始
            while s[i] in s[start:]:  # 如果有可能是回文
                j = s.index(s[i], start)  # 从start开始第一个等于s[i]的索引
                # 检查 s[i:j+1] 是不是回文串
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l, r = l + 1, r - 1
                # 如果是就dfs
                if l >= r:
                    dfs(j + 1, path + [s[i : j + 1]])
                # 继续检查更长的
                start = j + 1

        res = []
        dfs(0, [])
        return res


# @lc code=end


func = Solution().partition
s = "aab"
print(func(s))
# [["a","a","b"],["aa","b"]]

s = "a"
print(func(s))
# [["a"]]
