# @lc app=leetcode.cn id=116 lang=python3
# [116] 填充每个节点的下一个右侧节点指针
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/
# Medium (73.04%)
# Testcase Example:  '[1,2,3,4,5,6,7]'
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
# 示例 1：
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由
# next 指针连接，'#' 标志着每一层的结束。
# 示例 2:
# 输入：root = []
# 输出：[]
# 提示：
# 树中节点的数量在 [0, 2^12 - 1] 范围内
# -1000 <= node.val <= 1000
# 进阶：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

# @lc code=start
from typing import Optional
from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        def level(root):
            if not root:
                return None
            q = deque()
            q.append(root)
            while q:
                n = len(q)
                for i in range(n):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    if i > 0:
                        prev.next = cur
                    prev = cur
            return root

        def recursive(root):
            if not root:
                return None

            def connect(left, right):
                if not left or not right:
                    return
                left.next = right
                connect(left.left, left.right)
                connect(right.left, right.right)
                connect(left.right, right.left)

            connect(root.left, root.right)
            return root

        return recursive(root)


# @lc code=end
