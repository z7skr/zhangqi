# @lc app=leetcode.cn id=206 lang=python3
# [206] 反转链表
# https://leetcode.cn/problems/reverse-linked-list/description/
# Easy (74.29%)
# Testcase Example:  '[1,2,3,4,5]'
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 示例 1：
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 示例 2：
# 输入：head = [1,2]
# 输出：[2,1]
# 示例 3：
# 输入：head = []
# 输出：[]
# 提示：
# 链表中节点的数目范围是 [0, 5000]
# -5000
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import Optional, List

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)

    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev

    def traverse(self, head):
        dummy = ListNode()
        while head:
            cur = head
            head = head.next
            cur.next = dummy.next
            dummy.next = cur
        return dummy.next

    def recursive(self, head):
        if not head or not head.next:
            return head
        new_head = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def print(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


# @lc code=end


func = Solution().reverseList
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().print(func(head))
# [5,4,3,2,1]

head = ListNode(1, ListNode(2))
Solution().print(func(head))
# [2,1]

head = None
Solution().print(func(head))
# []
