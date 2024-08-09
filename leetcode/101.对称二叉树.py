# @lc app=leetcode.cn id=101 lang=python3
# [101] 对称二叉树
# https://leetcode.cn/problems/symmetric-tree/description/
# Easy (59.74%)
# Testcase Example:  '[1,2,2,3,4,4,3]'
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 提示：
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True

            def dfs(left, right):
                if not left and not right:
                    return True
                if not left or not right:
                    return False
                if left.val != right.val:
                    return False
                return dfs(left.left, right.right) and dfs(left.right, right.left)

            return dfs(root.left, root.right)

        def bfs(root):
            if not root:
                return True
            q = deque()
            q.append(root)
            while q:
                size = len(q)
                for i in range(size // 2):
                    j = size - 1 - i
                    if not q[i] and not q[j]:
                        pass
                    elif not q[i] or not q[j]:
                        return False
                    elif q[i].val != q[j].val:
                        return False
                for _ in range(size):
                    cur = q.popleft()
                    if cur:
                        q.append(cur.left)
                        q.append(cur.right)
            return True

        return bfs(root)


# @lc code=end
