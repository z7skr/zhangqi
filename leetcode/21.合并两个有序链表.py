# @lc app=leetcode.cn id=21 lang=python3
# [21] 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
# Easy (66.25%)
# Testcase Example:  '[1,2,4]\n[1,3,4]'
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 提示：
# 两个链表的节点数目范围是 [0, 50]
# -100
# l1 和 l2 均按 非递减顺序 排列

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.recursive(list1, list2)

    def traverse(self, list1, list2) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return dummy.next

    def recursive(self, list1, list2) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.recursive(list1, list2.next)
            return list2


# @lc code=end
