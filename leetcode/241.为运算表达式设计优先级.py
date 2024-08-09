# @lc app=leetcode.cn id=241 lang=python3
# [241] 为运算表达式设计优先级
# https://leetcode.cn/problems/different-ways-to-add-parentheses/description/
# Medium (75.53%)
# Testcase Example:  '"2-1-1"'
# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 10^4 。
# 示例 1：
# 输入：expression = "2-1-1"
# 输出：[0,2]
# 解释：
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2：
# 输入：expression = "2*3-4*5"
# 输出：[-34,-14,-10,-10,10]
# 解释：
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# 提示：
# 1 <= expression.length <= 20
# expression 由数字和算符 '+'、'-' 和 '*' 组成。
# 输入表达式中的所有整数值在范围 [0, 99]


# @lc code=start
class Solution:
    from typing import List

    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dfs(expression, {})

    def dfs(self, expression, memo):
        if expression in memo:
            return memo[expression]
        if expression.isdigit():
            memo[expression] = int(expression)
            return [memo[expression]]
        ret = []
        for i, c in enumerate(expression):
            if c in "+-*":
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i + 1 :])
                ret.extend(eval(f"{a}{c}{b}") for a in l for b in r)
        memo[expression] = ret
        return ret


# @lc code=end


func = Solution().diffWaysToCompute
expression = "2-1-1"
print(func(expression))
# [0,2]

expression = "2*3-4*5"
# 10 -14 -10 -10 -14 -34
print(func(expression))
# [-34,-14,-10,-10,10]
