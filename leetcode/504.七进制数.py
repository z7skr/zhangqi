# @lc app=leetcode.cn id=504 lang=python3
# [504] 七进制数
# https://leetcode.cn/problems/base-7/description/
# Easy (51.85%)
# Testcase Example:  '100'
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
# 示例 1:
# 输入: num = 100
# 输出: "202"
# 示例 2:
# 输入: num = -7
# 输出: "-10"
# 提示：
# -10^7 <= num <= 10^7


# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        x = abs(num)
        while x:
            res.append(str(x % 7))
            x //= 7
        if num < 0:
            res.append("-")
        return "".join(res[::-1])


# @lc code=end


func = Solution().convertToBase7
num = 100
print(func(num))
#  "202"

num = -7
print(func(num))
#  "-10"
