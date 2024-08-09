# @lc app=leetcode.cn id=83 lang=python3
# [83] 删除排序链表中的重复元素
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
# Easy (53.62%)
# Testcase Example:  '[1,1,2]'
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# 示例 1：
# 输入：head = [1,1,2]
# 输出：[1,2]
# 示例 2：
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
# 提示：
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        def recursive_delete(head):
            # 给定头结点, 返回去重后的链表头结点
            if not head or not head.next:
                return head
            if head.val == head.next.val:  # 如果当前节点=下个节点, 直接跳过第一个节点
                head = recursive_delete(head.next)
            else:  # 否则, 当前节点直接连接下个节点
                head.next = recursive_delete(head.next)
            return head

        # 遍历
        def traverse_delete(head):
            if not head:
                return head
            prev, node = head, head
            while node:
                # 不等于, prev就直接连到node
                # 等于, prev就不动
                if prev.val != node.val:
                    prev.next = node
                    prev = prev.next
                node = node.next
            prev.next = None
            return head

        return traverse_delete(head)


# @lc code=end
