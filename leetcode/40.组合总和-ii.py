# @lc app=leetcode.cn id=40 lang=python3
# [40] 组合总和 II
# https://leetcode.cn/problems/combination-sum-ii/description/
# Medium (59.54%)
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出: [[1,1,6],[1,2,5],[1,7],[2,6]]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出: [[1,2,2],[5]]
# 提示:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, t):
            if t == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # 第一个元素总是要dfs, 第二个重复元素如果再dfs就会重复
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if t < candidates[i]:  # 因为有序
                    break
                path.append(candidates[i])
                # 如果是 i+1 表示每个数只能用一次
                dfs(i + 1, t - candidates[i])
                path.pop()

        candidates.sort()
        res, path = [], []
        dfs(0, target)
        return res


# @lc code=end

func = Solution().combinationSum2
candidates = [1, 1, 2, 2]
target = 3
print(func(candidates, target))
# [[1, 2]]

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(func(candidates, target))
# 输出: [[1,1,6],[1,2,5],[1,7],[2,6]]

candidates = [2, 5, 2, 1, 2]
target = 5
print(func(candidates, target))
# 输出: [[1,2,2],[5]]
