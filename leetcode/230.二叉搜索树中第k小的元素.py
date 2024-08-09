# @lc app=leetcode.cn id=230 lang=python3
# [230] 二叉搜索树中第K小的元素
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
# Medium (77.57%)
# Testcase Example:  '[3,1,4,null,2]\n1'
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
# 示例 1：
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 示例 2：
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
# 提示：
# 树中的节点数为 n 。
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from typing import Optional

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        helper = [0, None]

        def dfs(root):
            if helper[1] is not None:
                return
            if not root:
                return
            dfs(root.left)
            v = root.val
            helper[0] += 1
            if helper[0] == k:
                helper[1] = v
            dfs(root.right)

        dfs(root)
        return helper[1]


# @lc code=end


func = Solution().kthSmallest
root = [3, 1, 4, null, 2]
k = 1
print(func(root, k))
# 1

root = [5, 3, 6, 2, 4, null, null, 1]
k = 3
print(func(root, k))
# 3
