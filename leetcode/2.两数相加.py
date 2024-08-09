# @lc app=leetcode.cn id=2 lang=python3
# [2] 两数相加
# https://leetcode.cn/problems/add-two-numbers/description/
# Medium (43.13%)
# Testcase Example:  '[2,4,3]\n[5,6,4]'
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例 1：
# 输入：l1 = [2,4,3,1], l2 = [5,6,4]
# 输出：[7,0,8,1]
# 解释：1342 + 465 = 1807.
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
# 提示：
# 每个链表中的节点数在范围 [1, 100] 内
# 0
# 题目数据保证列表表示的数字不含前导零

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def simple(l1, l2):
            dummy = ListNode(0)
            p1, p2, p = l1, l2, dummy
            add = 0
            while p1 and p2:
                add, val = divmod(p1.val + p2.val + add, 10)
                p.next = ListNode(val)
                p1, p2, p = p1.next, p2.next, p.next
            if p2:
                p1 = p2
            while p1:
                add, val = divmod(p1.val + add, 10)
                p.next = ListNode(val)
                p1, p = p1.next, p.next
            if add == 1:
                p.next = ListNode(add)
            return dummy.next

        return simple(l1, l2)
        # @lc code=end


func = Solution().addTwoNumbers
