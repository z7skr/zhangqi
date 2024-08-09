# @lc app=leetcode.cn id=921 lang=python3
# [921] 使括号有效的最少添加
# https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/description/
# Medium (73.10%)
# Testcase Example:  '"())"'
# 只有满足下面几点之一，括号字符串才是有效的：
# 它是一个空字符串，或者
# 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
# 它可以被写作 (A)，其中 A 是有效字符串。
# 给定一个括号字符串 s ，在每一次操作中，你都可以在字符串的任何位置插入一个括号
# 例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
# 返回 为使结果字符串 s 有效而必须添加的最少括号数。
# 示例 1：
# 输入：s = "())"
# 输出：1
# 示例 2：
# 输入：s = "((("
# 输出：3
# 提示：
# 1 <= s.length <= 1000
# s 只包含 '(' 和 ')' 字符。


# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        def f1(s):
            stack = []
            res = 0
            for i in s:
                if i == "(":
                    stack.append(i)
                else:
                    # 如果栈空
                    if not stack:
                        res += 1
                    # 不空说明是左括号
                    else:
                        stack.pop()
                    # 栈只有左括号，这说明不需要用栈结构
            return res + len(stack)

        def f2(s):
            stack = 0
            res = 0
            for i in s:
                if i == "(":
                    stack += 1
                else:
                    if stack == 0:
                        res += 1
                    else:
                        stack -= 1
            return res + stack

        return f1(s)


# @lc code=end
func = Solution().minAddToMakeValid

s = "())"
print(func(s))
# 输出：1

s = "((("
print(func(s))
# 输出：3
