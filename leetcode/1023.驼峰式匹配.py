# @lc app=leetcode.cn id=1023 lang=python3
# [1023] 驼峰式匹配
# https://leetcode.cn/problems/camelcase-matching/description/
# Medium (64.49%)
# Testcase Example:  '["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]\n"FB"'
# 给你一个字符串数组 queries，和一个表示模式的字符串 pattern，请你返回一个布尔数组 answer 。只有在待查项 queries[i]
# 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。
# 如果可以将小写字母插入模式串 pattern 得到待查询项
# query，那么待查询项与给定模式串匹配。可以在任何位置插入每个字符，也可以不插入字符。
# 示例 1：
# 输入：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FB"
# 输出：[true,false,true,true,false]
# 示例：
# "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
# "FootBall" 可以这样生成："F" + "oot" + "B" + "all".
# "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
# 示例 2：
# 输入：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBa"
# 输出：[true,false,true,false,false]
# 解释：
# "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
# "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
# 示例 3：
# 输入：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBaT"
# 输出：[false,true,false,false,false]
# 解释：
# "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
# 提示：
# 1 <= pattern.length, queries.length <= 100
# 1 <= queries[i].length <= 100
# queries[i] 和 pattern 由英文字母组成

# @lc code=start
class Solution:
    from typing import List
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pass
# @lc code=end


func = Solution().camelMatch
queries =
print(func(queries))
# [true,false,true,true,false]

queries =
print(func(queries))
# [true,false,true,false,false]

queries =
print(func(queries))
# [false,true,false,false,false]

