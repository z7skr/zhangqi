# @lc app=leetcode.cn id=90 lang=python3
# [90] 子集 II
# https://leetcode.cn/problems/subsets-ii/description/
# Medium (63.48%)
# Testcase Example:  '[1,2,2]'
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
# 提示：
# 1
# -10

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs1():
            def dfs(i):
                if i == len(nums):
                    res.append(path[:])
                    return
                # #1.先选
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
                # #2.后不选，如果相同就一直不选，不然第一个没选第二个选了就会有问题
                # 如果某个位置走#2了, 就必须跳过剩下的, 不然下一次还有两个选择就重复了
                while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                    i += 1
                dfs(i + 1)

            nums.sort()
            res, path = [], []
            dfs(0)
            return res

        def dfs2():
            # 重复的情况下(没有重复也一样), 对相同的n个数, 只区分个数而不是组合
            def dfs(i, path):
                if i == len(nums):
                    res.append(path)
                    return
                j = i  # j: 下一个不等于nums[i]的下标
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                # 对 k个i, path分别增加 0,1,..,k 个 i
                for n in range(j - i + 1):
                    dfs(j, path + [nums[i]] * n)

            nums.sort()
            res = []
            dfs(0, [])
            return res

        def dfs3():
            # 重复的情况下(没有重复也一样), 对相同的n个数, 只区分个数而不是组合
            def dfs(i):
                if i == len(nums):
                    res.append(path[:])
                    return
                j = i  # j: 下一个不等于nums[i]的下标
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                # 对 k个i, path分别增加 0,1,..,k 个 i
                dfs(i + 1)
                for n in range(1, j - i + 1):
                    for _ in range(n):
                        path.append(nums[i])
                    dfs(j)
                    for _ in range(n):
                        path.pop()

            nums.sort()
            res, path = [], []
            dfs(0)
            return res

        return dfs3()


# # @lc code=end
nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))
# [[],[1],[1,2],[1,2,2],[2],[2,2]]
