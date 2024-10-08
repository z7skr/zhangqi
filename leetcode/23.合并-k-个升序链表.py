# @lc app=leetcode.cn id=23 lang=python3
# [23] 合并 K 个升序链表
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
# Hard (58.86%)
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
# 输入：lists = []
# 输出：[]
# 示例 3：
# 输入：lists = [[]]
# 输出：[]
# 提示：
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4

# @lc code=start
# Definition for singly-linked list.
from itertools import count
from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def auto_increment():
            def counter():
                counter.i += 1
                return counter.i

            counter.i = 0
            return counter

        def auto_increment():
            s = [0]

            def counter():
                s[0] += 1
                return s[0]

            return counter

        f = auto_increment()

        if not lists:
            return None
        h = []
        i = 0
        for cur in lists:
            if cur:
                heapq.heappush(h, (cur.val, f(), cur))
                i += 1
        p = dummy = ListNode(0)
        while h:
            p.next = heapq.heappop(h)[2]
            p = p.next
            if p.next:
                cur = p.next
                heapq.heappush(h, (cur.val, f(), cur))
                i += 1
        return dummy.next


# # @lc code=end
