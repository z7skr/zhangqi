# @lc app=leetcode.cn id=670 lang=python3
# [670] 最大交换
# https://leetcode.cn/problems/maximum-swap/description/
# Medium (49.10%)
# Testcase Example:  '2736'
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
# 示例 1 :
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 示例 2 :
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
# 注意:
# 给定数字的范围是 [0, 10^8]


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s) - 1):
            if s[i] < s[i + 1]:
                break
        else:
            return num

        max_idx, max_val = i + 1, s[i + 1]
        for j in range(i + 1, len(s)):
            if max_val <= s[j]:
                max_idx, max_val = j, s[j]
        left_idx = i
        for j in range(i, -1, -1):
            if s[j] < max_val:
                left_idx = j
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]
        return int("".join(s))


# @lc code=end


func = Solution().maximumSwap

num = 2377
print(func(num))
# 输出: 7372

num = 9937
print(func(num))
# 输出: 9973

num = 20909
print(func(num))
# 输出: 90902

num = 998899
print(func(num))
# 输出: 999898

num = 98765
print(func(num))
# 输出: 999898
