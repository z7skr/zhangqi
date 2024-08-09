# @lc app=leetcode.cn id=295 lang=python3
# [295] 数据流的中位数
# https://leetcode.cn/problems/find-median-from-data-stream/description/
# Hard (54.25%)
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' + '[[],[1],[2],[],[3],[]]'
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^-5 以内的答案将被接受。
# 示例 1：
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 提示:
# -10^5 <= num <= 10^5
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 10^4 次调用 addNum 和 findMedian
# @lc code=start
import heapq


class MedianFinder:
    def __init__(self):
        self.q1 = [1000000]  # 小值大堆,相反数 # 6 6 5 4
        self.q2 = [1000000]  # 大值小堆, # 8 8 9 10

    def addNum(self, num: int) -> None:
        if self.q2[0] < num:
            heapq.heappush(self.q2, num)
        else:
            heapq.heappush(self.q1, -num)

        if len(self.q1) - len(self.q2) == 2:
            heapq.heappush(self.q2, -heapq.heappop(self.q1))
        elif len(self.q2) - len(self.q1) == 2:
            heapq.heappush(self.q1, -heapq.heappop(self.q2))

    def findMedian(self) -> float:
        if len(self.q1) - len(self.q2) > 0:
            return -self.q1[0]
        elif len(self.q1) - len(self.q2) < 0:
            return self.q2[0]
        else:
            return (self.q2[0] - self.q1[0]) / 2


from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
            # 保证push进large的值都比small的大
        else:
            heappush(self.small, -heappushpop(self.large, num))
            # 保证push进small的值都比large的小

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# @lc code=end

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())  # 1.5
obj.addNum(3)
print(obj.findMedian())  # 2
