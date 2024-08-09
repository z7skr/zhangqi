# @lc app=leetcode.cn id=22 lang=python3
# [22] 括号生成
# https://leetcode.cn/problems/generate-parentheses/description/
# Medium (77.67%)
# Testcase Example:  '3'
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
# 输入：n = 1
# 输出：["()"]
# 提示：
# 1 <= n <= 8


# @lc code=start
class Solution:
    from typing import List

    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, tmp):
            if l == 0 and r == 0:
                res.append(tmp)
            elif l == 0:
                dfs(l, r - 1, tmp + ")")
            elif l == r:
                dfs(l - 1, r, tmp + "(")
            else:
                dfs(l - 1, r, tmp + "(")
                dfs(l, r - 1, tmp + ")")

        res = []
        dfs(n, n, "")
        return res


# @lc code=end


func = Solution().generateParenthesis

n = 1
print(func(n))
# ["()"]

n = 2
print(func(n))
# ["()()","(())"]
n = 3
print(func(n))
# ["()()()","(()())","((()))","(())()","()(())",]


n = 4
print(func(n))
# ["(())(())","(((())))","((()))()","()((()))","((())())","(())()()","()(())()","(()(()))","()()(())","((()()))","(()())()","()(()())","(()()())","()()()()"]
