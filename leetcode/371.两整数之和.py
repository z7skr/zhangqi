# @lc app=leetcode.cn id=371 lang=python3
# [371] 两整数之和
# https://leetcode.cn/problems/sum-of-two-integers/description/
# Medium (62.58%)
# Testcase Example:  '1\n2'
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。
# 示例 1：
# 输入：a = 1, b = 2
# 输出：3
# 示例 2：
# 输入：a = 2, b = 3
# 输出：5
# 提示：
# -1000 <= a, b <= 1000


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 无进位加法: a ^ b
        # 进位的部分: a & b
        # 进位的结果: (a & b) << 1
        # works both as while loop and single value check
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b  # 无进位加法
            b = carry  # 进位部分
        # handles overflow
        return (a & mask) if b > 0 else a


# @lc code=end


func = Solution().getSum
a = 1
b = 2
print(func(a, b))
# 3

a = 2
b = 3
print(func(a, b))
# 5


print(0b10, bin(2))
print(0o10, oct(8))
print(0x10, hex(16))
