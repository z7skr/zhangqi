# @lc app=leetcode.cn id=135 lang=python3
# [135] 分发糖果
# https://leetcode.cn/problems/candy/description/
# Hard (48.91%)
# Testcase Example:  '[1,0,2]'
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
# 示例 1：
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例 2：
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
# 提示：
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4


# @lc code=start
class Solution:
    from typing import List

    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)  # 左右冲突时，保持最高的那个
        return sum(res)


# @lc code=end


func = Solution().candy

ratings = [1, 0, 2]
print(func(ratings))
# 5

ratings = [1, 2, 2]
print(func(ratings))
# 4

ratings = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
print(func(ratings))
# 64

ratings = [1, 3, 4, 5, 2]  # [1,2,3,4,1]
print(func(ratings))
# 11
