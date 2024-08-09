# @lc app=leetcode.cn id=104 lang=python3
# [104] 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
# Easy (77.28%)
# Testcase Example:  '[3,9,20,null,null,15,7]'
# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 示例 2：
# 输入：root = [1,null,2]
# 输出：2
# 提示：
# 树中节点的数量在 [0, 10^4] 区间内。
# -100 <= Node.val <= 100

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        def bfs(root: Optional[TreeNode]):
            if not root:
                return 0
            q = deque()
            q.append(root)
            res = 0
            while q:
                res += 1
                size = len(q)
                for _ in range(size):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return res

        return bfs(root)


# @lc code=end
