# @lc app=leetcode.cn id=19 lang=python3
# [19] 删除链表的倒数第 N 个结点
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
# Medium (46.98%)
# Testcase Example:  '[1,2,3,4,5]\n2'
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]
# 提示：
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 进阶：你能尝试使用一趟扫描实现吗？

# @lc code=start
# Definition for singly-linked list.
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    p = head
    while p:
        print(p.val, end=" ")
        p = p.next
    print()


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 递归删除
        index_inverted = [0]  # 递归返回时开始增加

        def recursive_remove(head: ListNode, n):
            # 返回删除了倒数第n个节点的列表头结点
            if not head:
                return head
            head.next = recursive_remove(head.next, n)
            index_inverted[0] += 1  # 回溯时, 记录当前节点是倒数第几个
            # 如果是倒数第n个, 就返回head.next, 否则正常返回head
            return head.next if index_inverted[0] == n else head

        # 遍历
        def traverse_remove(head: ListNode, n):
            # 找到倒数第n个: fast从head起先走n步, 然后slow从head起和fast一起走到fast=None, slow就指向倒数第n个了
            # 如果要找到倒数第n个的前置节点, slow起点改成dummy就可以嘞
            dummy = ListNode(0, next=head)
            slow, fast = dummy, head
            for _ in range(n):
                fast = fast.next
            while fast:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return dummy.next

        # 利用栈结构, 全部进栈, 出栈的第n个元素就是需要删除的点, 此时栈顶就是前置
        def stack_remove(head: ListNode, n):
            dummy = ListNode(0, head)
            stack = []
            cur = dummy
            while cur:
                stack.append(cur)
                cur = cur.next
            for _ in range(n):
                stack.pop()
            prev = stack[-1]
            prev.next = prev.next.next
            return dummy.next

        return recursive_remove(head, n)


# @lc code=end
