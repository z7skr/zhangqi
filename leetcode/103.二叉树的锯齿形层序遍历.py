# @lc app=leetcode.cn id=103 lang=python3
# [103] 二叉树的锯齿形层序遍历
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
# Medium (58.62%)
# Testcase Example:  '[3,9,20,null,null,15,7]'
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
# 示例 2：
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
# 输入：root = []
# 输出：[]
# 提示：
# 树中节点数目在范围 [0, 2000] 内
# -100 <= Node.val <= 100

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            tmp = []
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res
