# @lc app=leetcode.cn id=700 lang=python3
# [700] 二叉搜索树中的搜索
# https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
# Easy (77.93%)
# Testcase Example:  '[4,2,7,1,3]\n2'
# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
# 示例 1:
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]
# 示例 2:
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[]
# 提示：
# 树中节点数在 [1, 5000] 范围内
# 1 <= Node.val <= 10^7
# root 是二叉搜索树
# 1 <= val <= 10^7

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchBST2(root, val)

    def searchBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node and node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right
        return node

    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > val:
            return self.searchBST2(root.left, val)
        elif root.val < val:
            return self.searchBST2(root.right, val)
        else:
            return root


# @lc code=end
