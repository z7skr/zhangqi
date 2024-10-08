# @lc app=leetcode.cn id=89 lang=python3
# [89] 格雷编码
# https://leetcode.cn/problems/gray-code/description/
# Medium (75.40%)
# Testcase Example:  '2'
# n 位格雷码序列 是一个由 2^n 个整数组成的序列，其中：
# 每个整数都在范围 [0, 2^n - 1] 内（含 0 和 2^n - 1）
# 第一个整数是 0
# 一个整数在序列中出现 不超过一次
# 每对 相邻 整数的二进制表示 恰好一位不同 ，且
# 第一个 和 最后一个 整数的二进制表示 恰好一位不同
# 给你一个整数 n ，返回任一有效的 n 位格雷码序列 。
# 示例 1：
# 输入：n = 2
# 输出：[0,1,3,2]
# 解释：
# [0,1,3,2] 的二进制表示是 [00,01,11,10] 。
# - 00 和 01 有一位不同
# - 01 和 11 有一位不同
# - 11 和 10 有一位不同
# - 10 和 00 有一位不同
# [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
# - 00 和 10 有一位不同
# - 10 和 11 有一位不同
# - 11 和 01 有一位不同
# - 01 和 00 有一位不同
# 示例 2：
# 输入：n = 1
# 输出：[0,1]
# 提示：
# 1 <= n <= 16


# @lc code=start
class Solution:
    from typing import List

    def grayCode(self, n: int) -> List[int]:
        res = [0] * (1 << n)
        for bit in range(1, n + 1):
            start, end = 1 << (bit - 1), 1 << bit
            for i in range(start, end):
                res[i] = start + res[end - 1 - i]
        return res


# @lc code=end

func = Solution().grayCode

n = 1
print(func(n))
# [0,1]
# 0, 1

n = 2
print(func(n))
# [0,1,3,2]
# 00,01,11,10

n = 3
print(func(n))
# [0,1,3,2,6,7,5,4]
# 000,001,011,010,110,111,101,100
