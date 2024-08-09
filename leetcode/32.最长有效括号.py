# @lc app=leetcode.cn id=32 lang=python3
# [32] 最长有效括号
# https://leetcode.cn/problems/longest-valid-parentheses/description/
# Hard (37.63%)
# Testcase Example:  '"(()"'
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
# 示例 1：
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：
# 输入：s = ""
# 输出：0
# 提示：
# 0
# s[i] 为 '(' 或 ')'


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def f1():
            stack = []
            l = ["0"] * len(s)
            for i, c in enumerate(s):
                if c == "(":
                    stack.append(i)
                else:
                    if stack:
                        l[stack.pop()] = "1"
                        l[i] = "1"
            return max(len(i) for i in "".join(l).split("0"))

        def dp():
            if not s:
                return 0
            n = len(s)
            dp = [0] * n
            for i in range(1, n):
                if s[i] == "(":
                    continue
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                else:
                    j = i - 1 - dp[i - 1]  # dp[i-1]的开头的前一位
                    if j >= 0 and s[j] == "(":
                        dp[i] = dp[i - 1] + 2 + dp[j - 1]
            return max(dp)

        return dp()


# @lc code=end

s = ")()())()((())()(())"
print(Solution().longestValidParentheses(s))
