# @lc app=leetcode.cn id=106 lang=python3
# [106] 从中序与后序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Medium (71.80%)
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
# 示例 1:
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
# 示例 2:
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
# 提示:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder, ib, ie, postorder, pb, pe):
            if ib > ie:
                return None
            for i in range(ib, ie + 1):
                if postorder[pe] == inorder[i]:
                    break
            return TreeNode(
                val=postorder[pe],
                left=build(inorder, ib, i - 1, postorder, pb, pb - ib + i - 1),
                right=build(inorder, i + 1, ie, postorder, pb - ib + i, pe - 1),
            )

        return build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


# @lc code=end
