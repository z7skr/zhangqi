# @lc app=leetcode.cn id=149 lang=python3
# [149] 直线上最多的点数
# https://leetcode.cn/problems/max-points-on-a-line/description/
# Hard (40.25%)
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 示例 1：
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 示例 2：
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 提示：
# 1
# points[i].length == 2
# -10^4 i, yi
# points 中的所有点 互不相同

# @lc code=start
from collections import defaultdict
from re import L
class Solution:
    from typing import List
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        res = 0
        def get_k(p1, p2):
            if p1[0] == p2[0]:
                return float('inf')
            return (p1[1] - p2[1]) / (p1[0] - p2[0])
        for i in range(len(points)):
            ks = defaultdict(int)
            for j in range(len(points)):
                if j == i:
                    continue
                k = get_k(points[i], points[j])
                ks[k] += 1
                res = max(res, ks[k] + 1)
        return res
# @lc code=end
func = Solution().maxPoints

points = [[1,1],[2,2],[3,3]]
print(func(points))
# 3

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(func(points))
# 4


points = [[1,1],[1,2],[1,3]]
print(func(points))
# 3


points = [[4,5],[4,-1],[4,0]]
print(func(points))
# 3
