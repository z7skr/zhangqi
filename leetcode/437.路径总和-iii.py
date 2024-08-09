# @lc app=leetcode.cn id=437 lang=python3
# [437] 路径总和 III
# https://leetcode.cn/problems/path-sum-iii/description/
# Medium (47.63%)
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 示例 1：
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
# 示例 2：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
# 提示:
# 二叉树的节点个数的范围是 [0,1000]
# -10^9
# -1000


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    from typing import Optional

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse():
            def computeLastSum(nums, target):
                res = [nums[-1] for _ in range(len(nums))]
                for i in reversed(range(len(nums) - 1)):
                    res[i] = res[i + 1] + nums[i]
                return res.count(target)

            def traverse(root):
                nonlocal res
                if not root:
                    return
                path.append(root.val)
                res += computeLastSum(path, targetSum)
                traverse(root.left)
                traverse(root.right)
                path.pop()

            path = []
            res = 0
            traverse(root)
            return res

        def dfs():
            sums = defaultdict(int)
            sums[0] = 1

            def dfs(root, total):
                count = 0
                if root:
                    total += root.val  # 当前从根节点下来的sum
                    count = sums[total - targetSum]
                    sums[total] += 1  # 下一步要用到的前缀和
                    count += dfs(root.left, total) + dfs(root.right, total)
                    sums[total] -= 1  # 用完了就撤销

                return count

            res = dfs(root, 0)
            print(sums)
            return res

        return dfs()


# @lc code=end


func = Solution().pathSum
root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]
targetSum = 8
print(func(root, targetSum))
# 3

root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
targetSum = 22
print(func(root, targetSum))
# 3
