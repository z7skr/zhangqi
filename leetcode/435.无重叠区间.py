# @lc app=leetcode.cn id=435 lang=python3
# [435] 无重叠区间
# https://leetcode.cn/problems/non-overlapping-intervals/description/
# Medium (51.68%)
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回
# 需要移除区间的最小数量，使剩余区间互不重叠 。
# 示例 1:
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 提示:
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4


# @lc code=start
class Solution:
    from typing import List

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def f1():
            intervals.sort()
            res = 0
            i, j = 0, 1
            while j < len(intervals):
                if intervals[i][1] > intervals[j][0]:
                    res += 1
                    if intervals[i][1] >= intervals[j][1]:  # 删i
                        i = j
                        j += 1
                    else:  # 删j
                        j += 1
                else:  # 不删
                    i = j
                    j += 1
            return res

        def f2():
            intervals.sort()
            res, i = 0, 0
            for j in range(1, len(intervals)):
                if intervals[i][1] > intervals[j][0]:
                    res += 1
                    if intervals[i][1] >= intervals[j][1]:  # 删i
                        i = j
                else:  # 不删
                    i = j
            return res

        return f2()


# @lc code=end


func = Solution().eraseOverlapIntervals
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(func(intervals))
#  1

intervals = [[1, 2], [1, 2], [1, 2]]
print(func(intervals))
#  2

intervals = [[1, 2], [2, 3]]
print(func(intervals))
#  0

intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
print(func(intervals))
# 2
# 0 1 2
#   1 2 3
#     2 3 4
#       3 4 5
#         4 5 6

intervals = [
    [-73, -26],
    [-65, -11],
    [-63, 2],
    [-62, -49],
    [-52, 31],
    [-40, -26],
    [-31, 49],
    [58, 95],
    [66, 98],
    [30, 47],
    [82, 97],
    [95, 99],
]
print(func(intervals))
# 7
