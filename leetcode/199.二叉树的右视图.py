# @lc app=leetcode.cn id=199 lang=python3
# [199] 二叉树的右视图
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
# Medium (66.62%)
# Testcase Example:  '[1,2,3,null,5,null,4]'
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 示例 1:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 示例 2:
# 输入: [1,null,3]
# 输出: [1,3]
# 示例 3:
# 输入: []
# 输出: []
# 提示:
# 二叉树的节点个数的范围是 [0,100]
# -100


# @lc code=start
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import List, Optional

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs():
            if not root:
                return []
            res = []
            q = deque([root])
            while q:
                size = len(q)
                res.append(q[-1].val)
                for _ in range(size):
                    c = q.popleft()
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
            return res

        def dfs():
            # 前序遍历, 结合深度, 第一次到 x 层时必是最左边 or 最右边的节点
            if not root:
                return []
            res = []

            def dfs(root, height):
                if not root:
                    return
                if len(res) == height:
                    res.append(root.val)
                if root.right:
                    dfs(root.right, height + 1)
                if root.left:
                    dfs(root.left, height + 1)

            dfs(root, 0)
            return res

        return bfs()


# @lc code=end

func = Solution().rightSideView

root = TreeNode(
    1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4))
)
print(func(root))
# [1,3,4]
root = TreeNode(1, right=TreeNode(3))
print(func(root))
# [1,3]
root = None
print(func(root))
# []
