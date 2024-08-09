# @lc app=leetcode.cn id=738 lang=python3
# [738] 单调递增的数字
# https://leetcode.cn/problems/monotone-increasing-digits/description/
# Medium (50.81%)
# Testcase Example:  '10'
# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。
# 示例 1:
# 输入: n = 10
# 输出: 9
# 示例 2:
# 输入: n = 1234
# 输出: 1234
# 示例 3:
# 输入: n = 332
# 输出: 299
# 提示:
# 0 <= n <= 10^9


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                break
        else:
            return n
        for j in range(i, -1, -1):
            if j == 0 or s[j] != s[j - 1]:
                break
        for i in range(j, len(s)):
            if i == j:
                s[i] = str(int(s[i]) - 1)
            else:
                s[i] = "9"
        return int("".join(s))


# @lc code=end
func = Solution().monotoneIncreasingDigits
n = 123
print(func(n))
#  123

n = 321
print(func(n))
#  299

n = 323
print(func(n))
#  299

n = 343
print(func(n))
#  339

n = 1234567851234
print(func(n))
#   1234567799999

n = 1234567801234
print(func(n))
#   1234567799999

n = 12377741234
print(func(n))
#   12369999999

n = 1023
print(func(n))
#   999
