# @lc app=leetcode.cn id=703 lang=python3
# [703] 数据流中的第 K 大元素
# https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/
# Easy (52.59%)
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' + '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
# 示例：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [8,5,4,2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
# 提示：
# 1
# 0
# -10^4
# -10^4
# 最多调用 add 方法 10^4 次
# 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

# @lc code=start
from typing import List
import heapq


class KthLargest:
    # 维护一个长度不超过k的最小堆, 超过就把最小值pop, 到最后的堆顶就是第k大
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) == self.k + 1:
            heapq.heappop(self.q)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# @lc code=end

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
