# @lc app=leetcode.cn id=191 lang=python3
# [191] 位1的个数
# https://leetcode.cn/problems/number-of-1-bits/description/
# Easy (77.28%)
# Testcase Example:  '11'
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。
# 示例 1：
# 输入：n = 11
# 输出：3
# 解释：输入的二进制串 1011 中，共有 3 个设置位。
# 示例 2：
# 输入：n = 128
# 输出：1
# 解释：输入的二进制串 10000000 中，共有 1 个设置位。
# 示例 3：
# 输入：n = 2147483645
# 输出：30
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 30 个设置位。
# 提示：
# 1 <= n <= 2^31 - 1
# 进阶：
# 如果多次调用这个函数，你将如何优化你的算法？


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     res += n & 1
        #     n >>= 1
        # return res

        cnt = 0
        while n:
            n = n & (n - 1)  # 不断将n最右的1改成0
            cnt += 1
        return cnt


# @lc code=end


func = Solution().hammingWeight
n = 11
print(func(n))
# 3

n = 128
print(func(n))
# 1

n = 2147483645
print(func(n))
# 30
