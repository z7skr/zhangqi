# @lc app=leetcode.cn id=129 lang=python3
# [129] 求根节点到叶节点数字之和
# https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/
# Medium (70.33%)
# Testcase Example:  '[1,2,3]'
# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。
# 叶节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25
# 示例 2：
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
# 提示：
# 树中节点的数目在范围 [1, 1000] 内
# 0
# 树的深度不超过 10


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(root, t=0):
            t = t * 10 + root.val
            if root.left:
                preorder(root.left, t)
            if root.right:
                preorder(root.right, t)
            if not root.left and not root.right:
                res[0] += t

        res = [0]
        preorder(root)
        return res[0]


# @lc code=end

func = Solution().sumNumbers
root = [1, 2, 3]
root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
# 25
print(func(root))
root = [4, 9, 0, 5, 1]
root = TreeNode(
    4, left=TreeNode(9, left=TreeNode(5), right=TreeNode(1)), right=TreeNode(0)
)
# 1026
print(func(root))
