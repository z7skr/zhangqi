# @lc app=leetcode.cn id=25 lang=python3
# [25] K 个一组翻转链表
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
# Hard (68.11%)
# Testcase Example:  '[1,2,3,4,5]\n2'
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？


# @lc code=start
# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import List, Optional

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def traverse():
            def reverseNextK(prev, k):  # 反转 prev 后的 k 个元素并返回下一个 prev
                tail, p = prev, prev.next
                for _ in range(k):
                    cur = p
                    tail = tail.next
                    p = p.next
                    cur.next = prev.next
                    prev.next = cur
                tail.next = p
                return tail

            dummy = ListNode(0, head)
            prev, p = dummy, dummy.next
            i = 0
            while p:
                p, i = p.next, i + 1
                if i > 0 and i % k == 0:
                    prev = reverseNextK(prev, k)

            return dummy.next

        # return traverse()

        # 反转以 a 为头结点的链表 === 反转 a 到 null 之间的结点
        def reverseAll(a: ListNode, b=None) -> Optional[ListNode]:
            pre, cur, nxt = None, a, a
            while cur != b:
                nxt = cur.next
                cur.next = pre  # 逐个结点反转
                pre = cur  # 更新指针位置
                cur = nxt
            # 返回反转后的头结点
            return pre

        # 反转区间 [a, b) 的元素，左闭右开
        def reverse(a: ListNode, b: ListNode) -> Optional[ListNode]:
            pre, cur, nxt = None, a, a
            while cur != b:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def reverseKGroup(head: ListNode, k: int) -> Optional[ListNode]:
            if not head:
                return head
            a, b = head, head  # 区间 [a, b) 包含 k 个待反转元素
            for _ in range(k):
                if not b:  # 不足 k 个，不需要反转，base case
                    return head
                b = b.next
            new_head = reverse(a, b)  # 反转前 k 个元素
            a.next = reverseKGroup(b, k)  # 递归反转后续链表并连接起来
            return new_head

        return reverseKGroup(head, k)


# @lc code=end


def make_listnode(nums):
    return ListNode(nums[0], next=make_listnode(nums[1:])) if nums else None


def print_listnode(head, x=""):
    def print_list(head):
        if head:
            print(head.val, end=" ")
            print_list(head.next)

    print(f"{x}:", end=" ")
    print_list(head)
    print()


func = Solution().reverseKGroup
head = [1, 2, 3, 4, 5]
head = make_listnode(head)
# print_listnode(head)
k = 2
print_listnode(func(head, k))
# [2,1,4,3,5]

head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = make_listnode(head)
k = 3
print_listnode(func(head, k))
# [3,2,1,4,5]
