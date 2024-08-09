# @lc app=leetcode.cn id=16 lang=python3
# [16] 最接近的三数之和
# https://leetcode.cn/problems/3sum-closest/description/
# Medium (44.85%)
# Testcase Example:  '[-1,2,1,-4]\n1'
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 示例 1：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 提示：
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = sum(nums[:3])
        # 排序
        nums.sort()
        i = 0
        # i 递增
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                # 根据sum和target的关系确定搜索方向
                tmp = nums[i] + nums[left] + nums[right]
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    return target
                # 每次更新一下结果
                if abs(tmp - target) < abs(res - target):
                    res = tmp
        return res


# @lc code=end
