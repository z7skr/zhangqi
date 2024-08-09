# @lc app=leetcode.cn id=590 lang=python3
# [590] N 叉树的后序遍历
# https://leetcode.cn/problems/n-ary-tree-postorder-traversal/description/
# Easy (78.79%)
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
# 给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
# 示例 1：
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[5,6,3,2,4,1]
# 示例 2：
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
# 提示：
# 节点总数在范围 [0, 10^4] 内
# 0 <= Node.val <= 10^4
# n 叉树的高度小于或等于 1000
# 进阶：递归法很简单，你可以使用迭代法完成此题吗?

# @lc code=start
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:

        def recursive(root):
            if not root:
                return
            for c in root.children:
                recursive(c)
            res.append(root.val)

        res = []
        # recursive(root)
        # return res

        def preorder2postorder(root):
            res = []
            if not root:
                return res
            stack = [root]
            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.children:
                    stack += node.children

            return res[::-1]

        # return preorder2postorder(root)

        def postorder(root):
            res = []
            if not root:
                return res
            stack = [root]
            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.children:
                    stack += node.children

            return res[::-1]

        return postorder(root)


# @lc code=end
