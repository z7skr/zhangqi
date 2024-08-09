# @lc app=leetcode.cn id=139 lang=python3
# [139] 单词拆分
# https://leetcode.cn/problems/word-break/description/
# Medium (55.84%)
# Testcase Example:  '"leetcode"\n["leet","code"]'
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 提示：
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同


# @lc code=start
class Solution:
    from typing import List

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs():
            def dfs(s, wd, i):
                if i == len(s):
                    return True
                for w in wd:
                    if len(w) > len(s) - i:
                        pass
                    if s[i : i + len(w)] == w:
                        if dfs(s, wd, i + len(w)):
                            return True
                return False
            
            wordDict.sort(key=len)
            wd = wordDict[:1]
            for i in range(1, len(wordDict)):
                p = wordDict[i]
                if not dfs(p, wd, 0):
                    wd.append(p)

            wd = wd[::-1]
            return dfs(s, wd, 0)
        
        def dp():
            ok = [True]
            for i in range(1, len(s)+1):
                ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
            return ok[-1]
        
        def dp1():
            ok = [True] + [False] * len(s)
            for i in range(1, len(s)+1):
                for j in range(i):
                    if ok[j] and s[j:i] in wordDict:
                        ok[i] = True
                        break
            return ok[-1]
        

        return dp1()


# @lc code=end

func = Solution().wordBreak

# s = "leetcode"
# wordDict = ["leet", "code"]
# print(func(s, wordDict))
# # 输出: true

# s = "applepenapple"
# wordDict = ["apple", "pen"]
# print(func(s, wordDict))
# # 输出: true


# s = "leetcodcodeco"
# wordDict = ["leet", "code", "cod"]
# print(func(s, wordDict))
# # 输出: true

s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]

print(func(s, wordDict))
# 输出: False