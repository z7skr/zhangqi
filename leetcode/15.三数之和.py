# @lc app=leetcode.cn id=15 lang=python3
# [15] 三数之和
# https://leetcode.cn/problems/3sum/description/
# Medium (37.63%)
# Testcase Example:  '[-1,0,1,2,-1,-4]'
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
# 提示：
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序，剩下的问题是怎么剪枝
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        # 固定第一个数
        for i in range(n):
            # 第一个数大于0就不可能有了
            if nums[i] > 0:
                return res
            # 判断第一个数是否已经有重复, 有的话肯定是重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 左右指针加快搜索
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    # 遇到的第一个答案放进res
                    res.append([nums[i], nums[l], nums[r]])
                    # 如果第二个数有重复, 就直接跳过
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # 如果第三个数有重复, 也直接跳过
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # 同时跳
                    l += 1
                    r -= 1
        return res
# @lc code=end
