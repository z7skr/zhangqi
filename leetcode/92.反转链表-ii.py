# @lc app=leetcode.cn id=92 lang=python3
# [92] 反转链表 II
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
# Medium (56.14%)
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 提示：
# 链表中节点数目为 n
# 1
# -500
# 1
# 进阶： 你可以使用一趟扫描完成反转吗？

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(ls):
    return ListNode(ls[0], build(ls[1:])) if ls else None


def print_ll(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            return head
        last = self.reverseN(head.next, n - 1)
        successor = head.next.next
        head.next.next = head
        head.next = successor
        return last

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


# @lc code=end


head = build([1, 2, 3, 4, 5])
left = 2
right = 4
print_ll(Solution().reverse(head))
# print_ll(Solution().reverseN(head, left))
# print_ll(Solution().reverseBetween(head, left, right))
# [1,4,3,2,5]

head = build([1, 2, 3, 4, 5])
left = 3
right = 5
print_ll(Solution().reverse(head))
# print_ll(Solution().reverseN(head, left))
# print_ll(Solution().reverseBetween(head, left, right))
# [1, 2, 5, 4, 3]
