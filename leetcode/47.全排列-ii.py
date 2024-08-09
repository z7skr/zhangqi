# @lc app=leetcode.cn id=47 lang=python3
# [47] 全排列 II
# https://leetcode.cn/problems/permutations-ii/description/
# Medium (65.68%)
# Testcase Example:  '[1,1,2]'
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 提示：
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs1():
            def dfs(nums, path):
                if not nums:
                    res.append(path)
                for i in range(len(nums)):
                    # 如果当前值=上一个值, 就该剪枝
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    dfs(nums[:i] + nums[i + 1 :], path + [nums[i]])

            res = []
            nums.sort()
            dfs(nums, [])
            return res

        def dfs2():
            def dfs(nums, start):
                if start == len(nums):
                    res.append(nums[:])
                for i in range(start, len(nums)):
                    # 1 2 2
                    if i > start and nums[start] == nums[i]:
                        continue
                    nums[start], nums[i] = nums[i], nums[start]
                    dfs(nums[:], start + 1)

            res = []
            nums.sort()
            dfs(nums, 0)
            return res

        return dfs2()


# @lc code=end
nums = [1, 2, 2]
# 1,2a,2b;  1,2b,2a --> 1,2,2
print(Solution().permuteUnique(nums))
