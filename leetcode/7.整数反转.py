# @lc app=leetcode.cn id=7 lang=python3
# [7] 整数反转
# https://leetcode.cn/problems/reverse-integer/description/
# Medium (35.44%)
# Testcase Example:  '123'
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
# 输入：x = 123
# 输出：321
# 示例 2：
# 输入：x = -123
# 输出：-321
# 示例 3：
# 输入：x = 120
# 输出：21
# 示例 4：
# 输入：x = 0
# 输出：0
# 提示：
# -2^31


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        f = 1 if x > 0 else -1
        x = x if x > 0 else -x
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        res = f * res
        if res < -1 << 31 or res >= 1 << 31:
            return 0
        return res


# @lc code=end
