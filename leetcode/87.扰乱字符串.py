# @lc app=leetcode.cn id=87 lang=python3
# [87] 扰乱字符串
# https://leetcode.cn/problems/scramble-string/description/
# Hard (47.07%)
# Testcase Example:  '"great"\n"rgeat"'
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
# 如果字符串的长度为 1 ，算法停止
# 如果字符串的长度 > 1 ，执行下述步骤：
# 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y
# 。
# 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x
# 。
# 在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
# 给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：s1 = "great", s2 = "rgeat"
# 输出：true
# 解释：s1 上可能发生的一种情形是：
# "great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
# "gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
# "gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
# "g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
# "r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
# "r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
# 算法终止，结果字符串和 s2 相同，都是 "rgeat"
# 这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
# 示例 2：
# 输入：s1 = "abcde", s2 = "caebd"
# 输出：false
# 示例 3：
# 输入：s1 = "a", s2 = "a"
# 输出：true
# 提示：
# s1.length == s2.length
# 1
# s1 和 s2 由小写英文字母组成


# @lc code=start
class Solution:
    # for storing already solved problems
    mp = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # Base cases
        if s1 == s2:
            return True
        if len(s1) != len(s1):
            return False
        key = s1 + " " + s2
        if key in self.mp:
            return self.mp[key]
        for i in range(1, len(s1)):
            # c1. not swap
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # c2. swap before next
            j = len(s1) - i
            if self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                return True

        self.mp[key] = False
        return False


# @lc code=end


func = Solution().isScramble
s1 = "great"
s2 = "rgeat"  # taerg
print(func(s1, s2))
# true

s1 = "abcde"
s2 = "caebd"
print(func(s1, s2))
# false

s1 = "a"
s2 = "a"
print(func(s1, s2))
# true

s1 = "abcdbdac"
s2 = "cdacabbd"
print(func(s1, s2))
# true

# abcd  bdac
# acdb
s1 = "abcdd"
s2 = "dbdac"
print(func(s1, s2))
# false


s1 = "fldiodffghyq"  # abcdefgh
s2 = "dgyhfqfdliof"  # efghabcd
print(func(s1, s2))
# true

s1 = "hobobyrqd"
s2 = "hbyorqdbo"
