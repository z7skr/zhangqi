# @lc app=leetcode.cn id=572 lang=python3
# [572] 另一棵树的子树
# https://leetcode.cn/problems/subtree-of-another-tree/description/
# Easy (47.56%)
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
# ；否则，返回 false 。
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
# 示例 1：
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
# 示例 2：
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
# 提示：
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4
# -10^4


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def is_same(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return is_same(t1.left, t2.left) and is_same(t1.right, t2.right)

        def is_sub(root):
            if not root:
                return False
            return (
                is_sub(root.left)
                or is_sub(root.right)
                or (root.val == subRoot.val and is_same(root, subRoot))
            )

        return is_sub(root)


# @lc code=end
func = Solution().isSubtree
root = TreeNode(
    3, left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)), right=TreeNode(5)
)
subRoot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
# true
print(func(root, subRoot))
root = TreeNode(
    3,
    left=TreeNode(4, left=TreeNode(1), right=TreeNode(2, right=TreeNode(0))),
    right=TreeNode(5),
)
subRoot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
# false
print(func(root, subRoot))
