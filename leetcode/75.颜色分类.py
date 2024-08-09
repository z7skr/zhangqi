# @lc app=leetcode.cn id=75 lang=python3
# [75] 颜色分类
# https://leetcode.cn/problems/sort-colors/description/
# Medium (61.50%)
# Testcase Example:  '[2,0,2,1,1,0]'
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
# 示例 1：
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 提示：
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
# 进阶：
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

# @lc code=start
class Solution:
    from typing import List
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def change():
            c0, c1 = nums.count(0), nums.count(1)
            for i in range(len(nums)):
                if i < c0:
                    nums[i] = 0
                elif i < c0 + c1:
                    nums[i] = 1
                else:
                    nums[i] = 2
        def swap():
            p0, p2 = 0, len(nums) - 1
            i = 0
            while i <= p2:
                if nums[i] == 0:
                    nums[i], nums[p0] = nums[p0], nums[i]
                    p0 += 1
                    i += 1
                elif nums[i] == 1:
                    i += 1
                elif nums[i] == 2:
                    nums[i], nums[p2] = nums[p2], nums[i]
                    p2 -= 1

        swap()
# @lc code=end

func = Solution().sortColors
nums = [2,0,2,1,1,0]
print(func(nums))
# [0,0,1,1,2,2]

nums = [2,0,1]
print(func(nums))
# [0,1,2]

