# @lc app=leetcode.cn id=132 lang=python3
# [132] 分割回文串 II
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
# Hard (49.79%)
# Testcase Example:  '"aab"'
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
# 返回符合要求的 最少分割次数 。
# 示例 1：
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 示例 2：
# 输入：s = "a"
# 输出：0
# 示例 3：
# 输入：s = "ab"
# 输出：1
# 提示：
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成


# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # cut numbers in worst case (no palindrome)
        n = len(s)
        cut = list(range(-1, n))  # cur[i] 是 s[:i] 的最小cut次数
        for i in range(n):
            # odd
            r = 0
            while i - r >= 0 and i + r < n and s[i - r] == s[i + r]:
                # 回文串的起点i终点j，那么f(s[:j+1])=cut[j+1]=1+cut[i]=1+f(s[:i])
                cut[i + r + 1] = min(cut[i + r + 1], cut[i - r] + 1)
                r += 1
            # even
            r = 0
            while i - r >= 0 and i + r + 1 < n and s[i - r] == s[i + r + 1]:
                cut[i + r + 2] = min(cut[i + r + 2], cut[i - r] + 1)
                r += 1
        # print(cut)
        return cut[n]


# @lc code=end


func = Solution().minCut

s = "a"
print(func(s))
# 0

s = "ab"
print(func(s))
# 1

s = "asasasasasbabab"
print(func(s))
# 2

# s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
# print(func(s))
# # # 452
