# @lc app=leetcode.cn id=958 lang=python3
# [958] 二叉树的完全性检验
# https://leetcode.cn/problems/check-completeness-of-a-binary-tree/description/
# Medium (54.74%)
# Testcase Example:  '[1,2,3,4,5,6]'
# 给你一棵二叉树的根节点 root ，请你判断这棵树是否是一棵 完全二叉树 。
# 在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。最后一层（第 h 层）中可以包含 1 到 2^h
# 个节点。
# 示例 1：
# 输入：root = [1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，节点值为 {1} 和 {2,3} 的两层），且最后一层中的所有节点（{4,5,6}）尽可能靠左。
# 示例 2：
# 输入：root = [1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的节点不满足条件「节点尽可能靠左」。
# 提示：
# 树中节点数目在范围 [1, 100] 内
# 1 <= Node.val <= 1000


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    from typing import Optional

    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                # 都进队
                # 拿出空的时候, 后面必须都是空
                if c:
                    q.append(c.left)
                    q.append(c.right)
                else:
                    for i in range(len(q)):
                        if q[i]:
                            return False
        return True


# @lc code=end

func = Solution().isCompleteTree
root = TreeNode(
    1,
    left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
    right=TreeNode(3, left=TreeNode(6)),
)
# true
print(func(root))
root = TreeNode(
    1,
    left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
    right=TreeNode(3, right=TreeNode(6)),
)
# false
print(func(root))
print(func(None))
