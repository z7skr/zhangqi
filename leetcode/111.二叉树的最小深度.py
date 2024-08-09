# @lc app=leetcode.cn id=111 lang=python3
# [111] 二叉树的最小深度
# https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/
# Easy (53.48%)
# Testcase Example:  '[3,9,20,null,null,15,7]'
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 示例 2：
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
# 提示：
# 树中节点数的范围在 [0, 10^5] 内
# -1000

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        q = deque()
        q.append(root)
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if not cur.left and not cur.right:
                    return res
        return res


# @lc code=end
