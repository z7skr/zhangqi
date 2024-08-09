# @lc app=leetcode.cn id=234 lang=python3
# [234] 回文链表
# https://leetcode.cn/problems/palindrome-linked-list/description/
# Easy (54.37%)
# Testcase Example:  '[1,2,2,1]'
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：
# 输入：head = [1,2]
# 输出：false
# 提示：
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        pass
        self.val = val
        self.next = next


from typing import Optional


# 1 2 3 4
#     s   f
# 1 2 3 4 5
#     s   f
class Solution:
    from typing import List
    def isPalindrome(self, head: ListNode) -> bool:
        pass
        def reverse(head):
            if not head or not head.next:
                return head
            tail = reverse(head.next)
            head.next.next = head
            head.next = None
            return tail

        if not head.next:
            return True
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        reverse(slow)
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True


# @lc code=end

func = Solution().__init__
head = [1,2,2,1]
print(func(head))
# true

head = [1,2]
print(func(head))
# false

