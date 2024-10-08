# @lc app=leetcode.cn id=415 lang=python3
# [415] 字符串相加
# https://leetcode.cn/problems/add-strings/description/
# Easy (54.53%)
# Testcase Example:  '"11"\n"123"'
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 示例 1：
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 示例 3：
# 输入：num1 = "0", num2 = "0"
# 输出："0"
# 提示：
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        res = []
        add = 0
        for i in range(max(l1, l2)):
            a = int(num1[i]) if i < l1 else 0
            b = int(num2[i]) if i < l2 else 0
            add, r = divmod(a + b + add, 10)
            res.append(str(r))
        if add == 1:
            res.append("1")
        return "".join(res[::-1])


# @lc code=end


func = Solution().addStrings
num1 = "11"
num2 = "123"
print(func(num1, num2))
# "134"

num1 = "456"
num2 = "77"
print(func(num1, num2))
# "533"

num1 = "0"
num2 = "0"
print(func(num1, num2))
# "0"
