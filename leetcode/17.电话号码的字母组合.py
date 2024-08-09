# @lc app=leetcode.cn id=17 lang=python3
# [17] 电话号码的字母组合
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
# Medium (58.95%)
# Testcase Example:  '"23"'
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：
# 输入：digits = ""
# 输出：[]
# 示例 3：
# 输入：digits = "2"
# 输出：["a","b","c"]
# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。

# @lc code=start
from typing import List
from unicodedata import digit


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }

        def dfs(digits, i, tmp):
            nonlocal res
            if i == len(digits):
                res.append(tmp)
            else:
                for c in mp[digits[i]]:
                    dfs(digits, i + 1, tmp + c)

        res = []
        dfs(digits, 0, "")
        return res


# @lc code=end
func = Solution().letterCombinations
digits = "23"
print(func(digits))
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits = ""
print(func(digits))
# 输出：[]
digits = "2"
print(func(digits))
# 输出：["a","b","c"]
