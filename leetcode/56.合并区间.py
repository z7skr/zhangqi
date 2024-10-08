# @lc app=leetcode.cn id=56 lang=python3
# [56] 合并区间
# https://leetcode.cn/problems/merge-intervals/description/
# Medium (49.72%)
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 提示：
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for cur in intervals[1:]:
            if res[-1][1] >= cur[0]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
        return res


# @lc code=end

func = Solution().merge

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(func(intervals))
# [[1,6],[8,10],[15,18]]

intervals = [[1, 4], [4, 5]]
print(func(intervals))
# [[1,5]]
