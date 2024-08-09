# @lc app=leetcode.cn id=10 lang=python3
# [10] 正则表达式匹配
# https://leetcode.cn/problems/regular-expression-matching/description/
# Hard (30.72%)
# Testcase Example:  '"aa"\n"a"'
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 示例 1：
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 示例 2:
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3：
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 提示：
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符


# @lc code=start


from operator import is_


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归, Time Limit Exceeded
        def recursive(s, p):
            if p == "":
                return s == ""
            if s == "":
                if len(p) >= 2 and p[1] == "*":
                    return recursive(s, p[2:])
                else:
                    return False
            if len(p) >= 2 and p[1] == "*":
                if p[0] == "." or p[0] == s[0]:
                    return (
                        recursive(s[1:], p[2:])
                        or recursive(s[1:], p)
                        or recursive(s, p[2:])
                    )
                else:
                    return recursive(s, p[2:])
            else:
                if p[0] == "." or p[0] == s[0]:
                    return recursive(s[1:], p[1:])
                else:
                    return False

        def dp(s, p):
            n, m = len(s), len(p)
            #  dp[i][j], is s[:i] and p[:j] match?
            dp = [[False] * (m + 1) for _ in range(n + 1)]
            dp[0][0] = True
            for i in range(0, n + 1):  # s从0开始
                for j in range(1, m + 1):  # p从1开始
                    if p[j - 1] != "*":  # p最后的字符不是*
                        dp[i][j] = (
                            i >= 1
                            and (
                                p[j - 1] == s[i - 1] or p[j - 1] == "."
                            )  # 最后一位匹配
                            and dp[i - 1][j - 1]  # 前面匹配
                        )
                    else:  # p最后的字符是*, j >= 1
                        dp[i][j] = dp[i][j - 2] or (  # *匹配0
                            i >= 1
                            and (p[j - 2] == s[i - 1] or p[j - 2] == ".")
                            and dp[i - 1][j]  # *再匹配s多一位
                        )
            return dp[n][m]

        return dp(s, p)


# @lc code=end
