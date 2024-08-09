# @lc app=leetcode.cn id=110 lang=python3
# [110] 平衡二叉树
# https://leetcode.cn/problems/balanced-binary-tree/description/
# Easy (58.13%)
# Testcase Example:  '[3,9,20,null,null,15,7]'
# 给定一个二叉树，判断它是否是 平衡二叉树
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 示例 2：
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 示例 3：
# 输入：root = []
# 输出：true
# 提示：
# 树中的节点数在范围 [0, 5000] 内
# -10^4 <= Node.val <= 10^4


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def isBalanced(self, root: TreeNode) -> bool:
        def isbalance(root=root, d=0):
            if not root:
                return 0, True  # depth, balance
            dl, bl = isbalance(root.left, d + 1)
            dr, br = isbalance(root.right, d + 1)
            return max(dl, dr) + 1, bl and br and abs(dl - dr) <= 1

        return isbalance()[1]


# @lc code=end

func = Solution().isBalanced
root = TreeNode(
    3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
)
print(func(root))
# true
root = TreeNode(
    1,
    left=TreeNode(
        2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)
    ),
    right=TreeNode(2),
)
# root = [1, 2, 2, 3, 3, null, null, 4, 4]
print(func(root))
# false
root = None
print(func(root))
# true
