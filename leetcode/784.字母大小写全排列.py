# @lc app=leetcode.cn id=784 lang=python3
# [784] 字母大小写全排列
# https://leetcode.cn/problems/letter-case-permutation/description/
# Medium (72.55%)
# Testcase Example:  '"a1b2"'
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
# 示例 1：
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 示例 2:
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
# 提示:
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成


# @lc code=start
class Solution:
    from typing import List

    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i):
            if i == len(chs):
                res.append("".join(chs))
                return
            if not chs[i].isalpha():
                dfs(i + 1)
            else:
                chs[i] = chs[i].lower()
                dfs(i + 1)
                chs[i] = chs[i].upper()
                dfs(i + 1)

        chs = list(s)
        res = []
        dfs(0)
        return res


# @lc code=end


func = Solution().letterCasePermutation
s = "a1b2"
print(func(s))
# ["a1b2", "a1B2", "A1b2", "A1B2"]

s = "3z4"
print(func(s))
#  ["3z4","3Z4"]
