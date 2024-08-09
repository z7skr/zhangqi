# @lc app=leetcode.cn id=91 lang=python3
# [91] 解码方法
# https://leetcode.cn/problems/decode-ways/description/
# Medium (33.64%)
# Testcase Example:  '"12"'
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
# 输入：s = "06"
# 输出：0
# 解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。
# 提示：
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # TLE
        def dfs():
            def dfs(i):
                nonlocal res
                if i == len(s):
                    res += 1
                    return
                if s[i] == "0":
                    return
                dfs(i + 1)
                if i + 1 < len(s) and int(s[i : i + 2]) < 27:
                    dfs(i + 2)

            res = 0
            dfs(0)
            return res

        def dp():
            n = len(s)
            dp = [0] * (n + 1)
            dp[0], dp[1] = 1, 0 if s[0] == "0" else 1
            for i in range(2, n + 1):
                if s[i - 1] == "0":
                    if s[i - 2] in "12":  # 10, 20
                        dp[i] = dp[i - 2]
                    else:  # 00, 30, 40, ...
                        return 0
                else:
                    # 01, 02, ..., 27, 28, ...
                    if s[i - 2] == "0" or int(s[i - 2 : i]) > 26:
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]

        def dp2():
            n = len(s)
            a, b, c = 1, 0 if s[0] == "0" else 1, 0
            for i in range(2, n + 1):
                if s[i - 1] == "0":
                    if s[i - 2] in "12":  # 10, 20
                        c = a
                    else:
                        return 0
                else:
                    if s[i - 2] == "0" or i > 1 and int(s[i - 2 : i]) > 26:
                        c = b
                    else:
                        c = a + b
                a, b = b, c
            return b

        def dp3():
            if s[0] == "0":
                return 0
            n = len(s)
            dp = [0] * (n + 1)
            dp[0], dp[1] = 1, 1
            for i in range(2, n + 1):
                if s[i - 1] == "0":
                    if s[i - 2] in "12":  # 10, 20
                        dp[i] = dp[i - 2]
                    else:  # 00, 30, 40, ...
                        return 0
                else:
                    # 01, 02, ..., 27, 28, ...
                    if s[i - 2] == "0" or int(s[i - 2 : i]) > 26:
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]

        def dp4():
            if not s:
                return 0
            n = len(s)
            dp = [0] * (n + 1)
            dp[0], dp[1] = 1, 0 if s[0] == "0" else 1
            for i in range(2, n + 1):
                if 1 <= int(s[i - 1 : i]) <= 9:  # (2)
                    dp[i] += dp[i - 1]
                if 10 <= int(s[i - 2 : i]) <= 26:  # (3)
                    dp[i] += dp[i - 2]
            return dp[n]

        def dp5():
            if not s:
                return 0
            n = len(s)
            a, b = 1, 0 if s[0] == "0" else 1
            for i in range(2, n + 1):
                r = 0
                if 1 <= int(s[i - 1 : i]) <= 9:  # (2)
                    r += b
                if 10 <= int(s[i - 2 : i]) <= 26:  # (3)
                    r += a
                a, b = b, r
            return b

        return dp2()


# @lc code=end


func = Solution().numDecodings
s = "22"  # 2 2; 22;
print(func(s))
# 2

s = "226"  # 2 2 6; 22 6; 2 26
print(func(s))
# 3

s = "220"  # 2 20;
print(func(s))
# 1

s = "222222"  #
print(func(s))
# 13

s = "10650"
print(func(s))
# 0

s = "2"  # 2
s = "22"  # 1 1; 11;
s = "222"  # 1 1 1 ; 11 1; 1 11
s = "228"  # 2 28
s = "2222"  # 1 1 1 1; 11 1 1; 1 11 1; 1 1 11; 11 11;
s = "22220"  # = '222'
s = "22228"  # = '2222'

# '111111' =
#   '111111 1'
#   '11111 11'
