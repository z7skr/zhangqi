# @lc app=leetcode.cn id=125 lang=python3
# [125] 验证回文串
# https://leetcode.cn/problems/valid-palindrome/description/
# Easy (46.94%)
# Testcase Example:  '"A man, a plan, a canal: Panama"'
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
# 示例 1：
# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
# 示例 2：
# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
# 示例 3：
# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。
# 提示：
# 1 <= s.length <= 2 * 10^5
# s 仅由可打印的 ASCII 字符组成


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isdigit():
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isdigit():
                j -= 1
            if i < j:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
        return True


# @lc code=end


func = Solution().isPalindrome

s = "A man, a plan, a canal: Panama"
print(func(s))
# 输出：true
s = "race a car"
print(func(s))
# 输出：false
s = " "
print(func(s))
# 输出：true
