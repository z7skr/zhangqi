# @lc app=leetcode.cn id=42 lang=python3
# [42] 接雨水
# https://leetcode.cn/problems/trapping-rain-water/description/
# Hard (63.22%)
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 提示：
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap_双指针_OnO1(height)

    def trap_动规_OnOn(self, height: List[int]) -> int:
        def trap(height):
            n = len(height)
            res = 0

            fs = [0] * n
            for i in range(1, n):
                fs[i] = max(fs[i - 1], height[i - 1])

            bs = [0] * n
            for i in reversed(range(n - 1)):
                bs[i] = max(bs[i + 1], height[i + 1])

            for i in range(n):
                res += max(0, min(fs[i], bs[i]) - height[i])
            return res

        return trap(height)

    def trap_双指针_OnO1(self, height: List[int]) -> int:
        def trap(height):
            n = len(height)
            res = 0
            l, r = 0, n - 1
            lmax, rmax = 0, 0
            while l <= r:
                lmax = max(lmax, height[l])
                rmax = max(rmax, height[r])
                if lmax < rmax:
                    # 左指针的右边至少有一个板子 > 左指针左边所有板子
                    # 根据水桶效应，保证了左指针当前列的水量决定权在左边
                    # 那么可以计算左指针当前列的水量：左边最大高度-当前列高度
                    res += lmax - height[l]
                    l += 1
                else:
                    res += rmax - height[r]
                    r -= 1
            return res

        return trap(height)


# @lc code=end
