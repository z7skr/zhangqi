# @lc app=leetcode.cn id=24 lang=python3
# [24] 两两交换链表中的节点
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
# Medium (72.18%)
# Testcase Example:  '[1,2,3,4]'
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 示例 1：
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
# 输入：head = []
# 输出：[]
# 示例 3：
# 输入：head = [1]
# 输出：[1]
# 提示：
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import List, Optional

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n1, n2, n3 = head, head.next, head.next.next
        n2.next = n1
        n1.next = self.swapPairs(n3)
        return n2

        # # 阴间玩意
        # p = head.next.next
        # head.next.next = head
        # head = head.next
        # head.next.next = p
        # head.next.next = self.swapPairs(p)
        # return head

    @classmethod
    def print(cls, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


# @lc code=end


func = Solution().swapPairs
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution.print(func(head))
# [2,1,4,3]

head = None
Solution.print(func(head))
# []

head = ListNode(1, ListNode(2, ListNode(3)))
Solution.print(func(head))
# [2,1,3]
