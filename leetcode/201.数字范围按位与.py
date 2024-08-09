# @lc app=leetcode.cn id=201 lang=python3
# [201] 数字范围按位与
# https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/
# Medium (54.53%)
# Testcase Example:  '5\n7'
# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right
# 端点）。
# 示例 1：
# 输入：left = 5, right = 7
# 输出：4
# 示例 2：
# 输入：left = 0, right = 0
# 输出：0
# 示例 3：
# 输入：left = 1, right = 2147483647
# 输出：0
# 提示：
# 0


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 101111010
        # 101011010 --> 101000000
        # 最高位连续的想同值
        res = 0
        i = 1
        while left >= i or right >= i:
            if left & i == right & i:
                res += left & i
            else:
                res = 0
            i <<= 1
        return res


# @lc code=end


func = Solution().rangeBitwiseAnd
left = 5
right = 7
# 101, 110, 111 -> 100
# 5的
print(func(left, right))
# 4

left = 0
right = 0
print(func(left, right))
# 0

left = 1
right = 2147483647
print(func(left, right))
# 0

left = 0
right = 1
print(func(left, right))
# 0

left = 10
# 1010, 1011
# 1010, 14: 1010
right = 11
print(func(left, right))
# 10


left = 15
# 1010, 1011
# 1010, 14: 1010
right = 15
print(func(left, right))
# 10
