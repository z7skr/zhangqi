# @lc app=leetcode.cn id=227 lang=python3
# [227] 基本计算器 II
# https://leetcode.cn/problems/basic-calculator-ii/description/
# Medium (44.75%)
# Testcase Example:  '"3+2*2"'
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
# 你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
# 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
# 示例 1：
# 输入：s = "3+2*2"
# 输出：7
# 示例 2：
# 输入：s = " 3/2 "
# 输出：1
# 示例 3：
# 输入：s = " 3+5 / 2 "
# 输出：5
# 提示：
# 1 <= s.length <= 3 * 10^5
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:

        def f1(s):
            stack_nums = []
            stack_sign = []
            i = 0
            tmp = ""
            s = s + "+0"
            while i < len(s):
                if s[i] == " ":
                    pass
                elif s[i] in ("+", "-", "*", "/"):
                    stack_nums.append(int(tmp))
                    tmp = ""
                    if stack_sign and stack_sign[-1] in ("*", "/"):
                        b, a = stack_nums.pop(), stack_nums.pop()
                        f = stack_sign.pop()
                        if f == "*":
                            stack_nums.append(a * b)
                        else:
                            stack_nums.append(a // b)
                    else:
                        pass
                    stack_sign.append(s[i])
                else:
                    tmp += s[i]
                i += 1
            stack_nums.append(int(tmp))
            res = stack_nums[0]
            i = 0
            for i in range(len(stack_sign)):
                if stack_sign[i] == "+":
                    res += stack_nums[i + 1]
                else:
                    res -= stack_nums[i + 1]
            return res

        def f2(s):
            stack, num, sign = [], 0, "+"
            for i in range(len(s)):
                if s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord("0")
                # sign 或者 末尾, sign 是 s[i] 前一个 sign
                if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                    if sign == "-":
                        stack.append(-num)
                    elif sign == "+":
                        stack.append(num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    else:
                        tmp = stack.pop()
                        if tmp // num < 0 and tmp % num != 0:
                            stack.append(tmp // num + 1)
                        else:
                            stack.append(tmp // num)
                    sign = s[i]  # next sign
                    num = 0
            return sum(stack)

        return f2(s)


# @lc code=end
s = "3+5/2*2-2*5"
print(Solution().calculate(s))
