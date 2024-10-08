# @lc app=leetcode.cn id=114 lang=python3
# [114] 二叉树展开为链表
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/
# Medium (73.35%)
# Testcase Example:  '[1,2,5,3,4,null,6]'
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
# 示例 1：
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
# 示例 2：
# 输入：root = []
# 输出：[]
# 示例 3：
# 输入：root = [0]
# 输出：[0]
# 提示：
# 树中结点数在范围 [0, 2000] 内
# -100
# 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flat2(root):
            # 定义: 原地按前序摊平二叉树
            # 分别摊平左右子树, 然后按照 root -> left -----> right 接起来
            if not root:
                return root
            flat(root.right)
            if root.left:
                flat(root.left)
                p = root.left
                while p.right:
                    p = p.right
                p.right = root.right
                root.right = root.left
                root.left = None

        def flat(root):
            if not root:
                return root
            left = flat(root.left)
            right = flat(root.right)
            if left is not None:
                root.left = None
                root.right = left
                p = left
                while p.right:
                    p = p.right
                p.right = right
            return root

        return flat(root)
        # return root


# @lc code=end
