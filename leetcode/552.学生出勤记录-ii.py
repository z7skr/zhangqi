# @lc app=leetcode.cn id=552 lang=python3
# [552] 学生出勤记录 II
# https://leetcode.cn/problems/student-attendance-record-ii/description/
# Hard (58.04%)
# Testcase Example:  '2'
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 10^9 + 7
# 取余 的结果。
# 示例 1：
# 输入：n = 2
# 输出：8
# 解释：
# 有 8 种长度为 2 的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
# 示例 2：
# 输入：n = 1
# 输出：3
# 示例 3：
# 输入：n = 10101
# 输出：183236316
# 提示：
# 1 <= n <= 10^5


# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        def dp1():
            # C[0] = no A, noa
            # C[1]: ends in 0 L = no A
            # C[2]: ends in 1 L = no A
            # C[3]: ends in 2 L = 1 A
            # C[4]: ends in 0 L = 1 A
            # C[5]: ends in 1 L = 1 A
            # ends in 2 Ls
            C, m = [1, 1, 0, 1, 0, 0], 10**9 + 7
            for _ in range(n - 1):
                a, b = sum(C[:3]) % m, sum(C[3:]) % m
                C = [a, C[0], C[1], a + b, C[3], C[4]]
            return sum(C) % m

        def dp2():
            MOD = 10**9 + 7
            dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]  # n,nA,last nL
            dp[0][0][0] = 1

            for i in range(1, n + 1):
                for j in range(2):
                    for k in range(3):
                        dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                # 以 A 结尾的数量
                for k in range(3):
                    dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

                # 以 L 结尾的数量
                for j in range(2):
                    for k in range(1, 3):
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

            total = 0
            for j in range(2):
                for k in range(3):
                    total = (total + dp[n][j][k]) % MOD
            return total

        return dp2()


# @lc code=end
func = Solution().checkRecord

n = 1
print(func(n))
# 3

n = 2
print(func(n))
# 8

n = 10101
print(func(n))
# 183236316
