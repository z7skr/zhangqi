# @lc app=leetcode.cn id=138 lang=python3
# [138] 随机链表的复制
# https://leetcode.cn/problems/copy-list-with-random-pointer/description/
# Medium (67.24%)
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
# 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
# --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 提示：
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        pass
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        def traverse():
            def recur(head):
                return Node(head.val, next=recur(head.next)) if head else None

            nhead = recur(head)
            d = {}
            p, q = head, nhead
            while p:
                d[p] = q
                p, q = p.next, q.next
            p, q = head, nhead
            while p:
                if p.random:
                    q.random = d[p.random]
                p, q = p.next, q.next
            return nhead

        def dfs():
            dct = {}

            def dfs(head):
                if not head:
                    return head
                if head in dct:
                    return dct[head]
                ret = Node(head.val)
                dct[head] = ret
                ret.next = dfs(head.next)
                ret.random = dfs(head.random)
                return ret

            return dfs(head)

        return dfs()


# @lc code=end


func = Solution().__init__
head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
print(func(head))
# [[7,null],[13,0],[11,4],[10,2],[1,0]]

head = [[1, 1], [2, 1]]
print(func(head))
# [[1,1],[2,1]]

head = [[3, null], [3, 0], [3, null]]
print(func(head))
# [[3,null],[3,0],[3,null]]
