# @lc app=leetcode.cn id=43 lang=python3
# [43] 字符串相乘
# https://leetcode.cn/problems/multiply-strings/description/
# Medium (44.30%)
# Testcase Example:  '"2"\n"3"'
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 提示：
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        res = []
        extra = 0
        for i in range(max(l1, l2)):
            a = int(num1[i]) if i < l1 else 0
            b = int(num2[i]) if i < l2 else 0
            extra, r = divmod(a + b + extra, 10)
            res.append(str(r))
        if extra == 1:
            res.append("1")
        return "".join(res[::-1])

    def mulStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return "0"
        L = len(num2)
        n, num = int(num1), num2[::-1]
        res = []
        extra = 0
        for i in range(L):
            a = int(num[i])
            extra, r = divmod(a * n + extra, 10)
            res.append(str(r))
        if extra != 0:
            res.append(str(extra))
        return "".join(res[::-1])

    def multiply1(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = "0"
        for i in range(len(num1)):
            for j in range(len(num2)):
                res = self.addStrings(
                    res,
                    str(int(num1[i]) * int(num2[j]))
                    + "0" * (len(num1) + len(num2) - i - j - 2),
                )
        return res

    def multiply2(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = "0"
        for i in range(len(num1)):
            add = self.mulStrings(num1[i], num2) + "0" * (len(num1) - i - 1)
            res = self.addStrings(res, add)
        return res

    def multiply(self, num1: str, num2: str) -> str:
        return self.multiply2(num1, num2)


# @lc code=end


func = Solution().multiply
num1 = "2"
num2 = "3"
print(func(num1, num2))
#  "6"

num1 = "123"
num2 = "456"
print(func(num1, num2))
#  "56088"
