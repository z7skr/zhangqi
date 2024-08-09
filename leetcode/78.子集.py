# @lc app=leetcode.cn id=78 lang=python3
# [78] 子集
# https://leetcode.cn/problems/subsets/description/
# Medium (81.20%)
# Testcase Example:  '[1,2,3]'
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
# 提示：
# 1
# -10
# nums 中的所有元素 互不相同

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            def dfs(i):
                if i == len(nums):
                    res.append(path[:])  # 复制
                else:
                    # 不加入
                    dfs(i + 1)
                    # 加入
                    path.append(nums[i])
                    dfs(i + 1)
                    path.pop()

            res, path = [], []
            dfs(0)
            return res

        def bit():
            res = []
            for num in range(1 << len(nums)):
                t = [nums[i] for i in range(len(nums)) if (num >> i) & 1]
                res.append(t)
            return res

        return bit()


# @lc code=end
func = Solution().subsets
nums = [1, 2, 3]
print(func(nums))
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
