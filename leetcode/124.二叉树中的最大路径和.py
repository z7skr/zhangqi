# @lc app=leetcode.cn id=124 lang=python3
# [124] 二叉树中的最大路径和
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
# Hard (45.42%)
# Testcase Example:  '[1,2,3]'
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 示例 1：
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
# 提示：
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 <= Node.val <= 1000


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def maxPathSum(self, root: TreeNode) -> int:
        def maxSumFromNode(node):
            l = maxSumFromNode(node.left) if node.left else 0
            r = maxSumFromNode(node.right) if node.right else 0
            maxSumPassbyNode = node.val + max(0, l, r, l + r)
            res[0] = max(res[0], maxSumPassbyNode)
            return node.val + max(0, l, r)

        res = [root.val]
        maxSumFromNode(root)
        return res[0]


# @lc code=end
