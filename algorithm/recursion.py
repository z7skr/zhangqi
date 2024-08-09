# 递归反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last

# 递归反转链表前 n 个节点
def reverseN(head, n: int):
    if n == 1:
        return head
    last = reverseN(head.next, n - 1)
    successor = head.next.next
    head.next.next = head
    head.next = successor
    return last

# 递归反转链表中第 left 到第 right 个节点
def reverseBetween(head, left: int, right: int):
    if left == 1:
        return reverseN(head, right)
    head.next = reverseBetween(head.next, left - 1, right - 1)
    return head



