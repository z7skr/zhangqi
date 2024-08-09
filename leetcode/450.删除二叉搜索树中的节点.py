# @lc app=leetcode.cn id=450 lang=python3
# [450] 删除二叉搜索树中的节点
# https://leetcode.cn/problems/delete-node-in-a-bst/description/
# Medium (52.32%)
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 一般来说，删除节点可分为两个步骤：
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 示例 1:
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 示例 2:
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
# 示例 3:
# 输入: root = [], key = 0
# 输出: []
# 提示:
# 节点数的范围 [0, 10^4].
# -10^5 <= Node.val <= 10^5
# 节点值唯一
# root 是合法的二叉搜索树
# -10^5 <= key <= 10^5
# 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    # 给定节点, 删除以这个节点为根节点的树中值为 key 的节点, 返回这棵树
    # 根节点可以被删除, 可以不存在这个 key 节点, 就原样返回
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 递归删除，对每个左右子树都返回相应的 deleteNode 返回值, 重新构建这棵树
        if not root:  # 找不到直接返回空
            return root
        if root.val > key:  # 在左子树去删除
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:  # 在右子树去删除
            root.right = self.deleteNode(root.right, key)
        else:
            # 如果不同时拥有左右子树，直接返回另一棵树即可
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 否则, 为了维护BST的性质就得把左子树的最大值or右子树的最小值拿上来
            drop = root.right
            while drop.left:
                drop = drop.left
            root.val = drop.val
            # 然后删除这个左子树的最大值or右子树的最小值, 这个值一定不同时拥有左右子树, 利用函数定义删除
            root.right = self.deleteNode(root.right, drop.val)
        return root


# @lc code=end
