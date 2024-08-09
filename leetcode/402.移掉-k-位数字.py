# @lc app=leetcode.cn id=402 lang=python3
# [402] 移掉 K 位数字
# https://leetcode.cn/problems/remove-k-digits/description/
# Medium (31.90%)
# Testcase Example:  '"1432219"\n3'
# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
# 示例 1 ：
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
# 示例 2 ：
# 输入：num = "10200", k = 1
# 输出："200"
# 解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 示例 3 ：
# 输入：num = "10", k = 2
# 输出："0"
# 解释：从原数字移除所有的数字，剩余为空就是 0 。
# 提示：
# 1
# num 仅由若干位数字（0 - 9）组成
# 除了 0 本身之外，num 不含任何前导零


# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        for _ in range(k):
            while i + 1 < len(num) and num[i] <= num[i + 1]:
                i += 1
            num = num[:i] + num[i + 1 :]
            if i > 0:  # 回退是防止i在最后
                i -= 1
            while num and num[0] == "0":
                num = num[1:]
        if not num:
            return "0"
        return num


# @lc code=end


func = Solution().removeKdigits
num = "1432219"
k = 3
print(func(num, k))
# "1219"

num = "10200"
k = 1
print(func(num, k))
# "200"

num = "10"
k = 2
print(func(num, k))
# "0"

num = "123456"
k = 3
print(func(num, k))
# "123"

num = "112"
k = 1
print(func(num, k))
# "11"

num = "111111"
k = 3
print(func(num, k))
# "111"

num = "1230"
k = 3
print(func(num, k))
# "0"
