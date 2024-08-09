# @lc app=leetcode.cn id=84 lang=python3
# [84] 柱状图中最大的矩形
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
# Hard (45.43%)
# Testcase Example:  '[2,1,5,6,2,3]'
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 示例 1:
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
# 输入： heights = [2,4]
# 输出： 4
# 提示：
# 1
# 0

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i, c in enumerate(heights):
            #       |
            #     | |
            #   | | |   |
            # | | | | . |
            #        c,i
            #       h*1
            #     h*2
            #   h*3
            # h*4
            # 出栈说明当前比较小，就以当前为界限
            while c < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans


# @lc code=end

heights = [1, 2, 3, 4, 3]
print(Solution().largestRectangleArea(heights))
