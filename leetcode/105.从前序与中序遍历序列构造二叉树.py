# @lc app=leetcode.cn id=105 lang=python3
# [105] 从前序与中序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Medium (71.19%)
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 示例 1:
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 示例 2:
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
# 提示:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, pb, pe, inorder, ib, ie):
            if pb > pe:
                return None
            i = inorder.index(preorder[pb])
            root = TreeNode(preorder[pb])
            root.left = build(preorder, pb + 1, pb - ib + i, inorder, ib, i - 1)
            root.right = build(preorder, pe - ie + i + 1, pe, inorder, i + 1, ie)
            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


# @lc code=end
