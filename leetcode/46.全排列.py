# @lc app=leetcode.cn id=46 lang=python3
# [46] 全排列
# https://leetcode.cn/problems/permutations/description/
# Medium (79.02%)
# Testcase Example:  '[1,2,3]'
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]
# 提示：
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs1():
            def dfs(nums, path):
                if not nums:
                    res.append(path)
                # 对每一个列表中的数, 当前加入path, 剩下的继续递归
                for i in range(len(nums)):
                    path.append(nums[i])
                    dfs(nums[:i] + nums[i + 1 :], path)

            res = []
            dfs(nums, [])
            return res

        def dfs2():
            def dfs(left):
                if left == len(nums):
                    res.append(nums[:])
                for i in range(left, len(nums)):
                    # 回溯
                    nums[left], nums[i] = nums[i], nums[left]
                    dfs(left + 1)
                    nums[left], nums[i] = nums[i], nums[left]

            res = []
            dfs(0)
            return res

        def dfs3():
            def dfs(nums, left):
                if left == len(nums):
                    res.append(nums)
                for i in range(left, len(nums)):
                    # 固定当前值, 剩下的继续递归, 和dfs1本质一样
                    nums[left], nums[i] = nums[i], nums[left]
                    dfs(nums[:], left + 1)  # 这里传值就不用撤销

            res = []
            dfs(nums, 0)
            return res

        return dfs3()


# @lc code=end
nums = [1, 2, 3]
print(Solution().permute(nums))
