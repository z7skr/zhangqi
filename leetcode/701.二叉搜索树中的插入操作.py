# @lc app=leetcode.cn id=701 lang=python3
# [701] 二叉搜索树中的插入操作
# https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/
# Medium (70.42%)
# Testcase Example:  '[4,2,7,1,3]\n5'
# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证
# ，新值和原始二叉搜索树中的任意节点值都不同。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
# 示例 1：
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[4,2,7,1,3,5]
# 解释：另一个满足题目要求可以通过的树是：
# 示例 2：
# 输入：root = [40,20,60,10,30,50,70], val = 25
# 输出：[40,20,60,10,30,50,70,null,null,25]
# 示例 3：
# 输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# 输出：[4,2,7,1,3,5]
# 提示：
# 树中的节点数将在 [0, 10^4]的范围内。
# -10^8 <= Node.val <= 10^8
# 所有值 Node.val 是 独一无二 的。
# -10^8 <= val <= 10^8
# 保证 val 在原始BST中不存在。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insertIntoBST2(root, val)

    # 真递归
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 给定root和val,返回插入了val的树
        if not root:
            return TreeNode(val)
        elif root.val > val:  # 左子树插入并返回
            root.left = self.insertIntoBST2(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST2(root.right, val)
        else:
            pass
        return root

    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        def insert(node, val):
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            elif node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)

        insert(root, val)
        return root


# @lc code=end
