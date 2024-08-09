# @lc app=leetcode.cn id=102 lang=python3
# [102] 二叉树的层序遍历
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
# Medium (66.73%)
# Testcase Example:  '[3,9,20,null,null,15,7]'
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
# 输入：root = []
# 输出：[]
# 提示：
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            res.append(tmp)
        return res


# @lc code=end
