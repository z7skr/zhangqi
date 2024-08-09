# @lc app=leetcode.cn id=698 lang=python3
# [698] 划分为k个相等的子集
# https://leetcode.cn/problems/partition-to-k-equal-sum-group/description/
# Medium (41.88%)
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 示例 1：
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 示例 2:
# 输入: nums = [1,2,3,4], k = 3
# 输出: false
# 提示：
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内


# @lc code=start
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        t = total // k  # 每个 group 的目标值
        if t < max(nums):
            return False
        nums.sort(reverse=True)

        def dfs1():
            # 依次将每个数放到某个 group 中
            def dfs(idx):
                if idx == len(nums):
                    return True
                for i in range(k):
                    if nums[idx] + group[i] <= t:
                        group[i] += nums[idx]
                        if dfs(idx + 1):
                            return True
                        group[i] -= nums[idx]
                        # 第一次将值添加到 group[i] 中且回溯失败, 意味着当前状态不可能成功.
                        # 因为不同的 group 是没区别的, 这个值总会进入一个 group.
                        # 在 group[i] 不能组成正确组合, 在之后的 group 也不能.
                        if group[i] == 0:
                            break

                return False

            group = [0] * k
            return dfs(0)

        def dfs2():
            # 对每个 group, 尝试怎么放入数, 再考虑下一个 group
            def dfs(k, s, start):
                # 还需要拼凑 k 个 group, 当前 group 的和为 s, 从 start 开始添加
                if k == 0:
                    return True
                if s == t:
                    return dfs(k - 1, 0, 0)
                for i in range(start, len(nums)):
                    if used[i]:
                        continue
                    used[i] = 1
                    s += nums[i]
                    if dfs(k, s, i + 1):
                        return True
                    used[i] = 0
                    s -= nums[i]
                    # 同上
                    if s == 0:
                        return False

                return False

            used = [0] * len(nums)
            return dfs(k, 0, 0)

        return dfs2()


# @lc code=end
# a = [1, 2, 3, 4, 5, 2, 3, 1, 4, 5, 1, 4]
# b = []
# nums = a + b
# k = 7
# print(Solution().canPartitionKgroup(nums, k))
