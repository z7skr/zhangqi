# @lc app=leetcode.cn id=912 lang=python3
# [912] 排序数组
# https://leetcode.cn/problems/sort-an-array/description/
# Medium (49.90%)
# Testcase Example:  '[5,2,3,1]'
# 给你一个整数数组 nums，请你将该数组升序排列。
# 示例 1：
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 提示：
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4

# @lc code=start
from math import ceil, log, log10
from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def less(x, y):
            return x < y

        # n2, 稳定
        def bubble_sort(nums):
            for turn in range(1, len(nums)):
                this_turn_not_exchanged = True
                for i in range(len(nums) - turn):
                    if less(nums[i + 1], nums[i]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        this_turn_not_exchanged = False
                if this_turn_not_exchanged:
                    break
            return nums

        # n2
        def bidirectinal_bubble_sort(nums):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                this_turn_not_exchanged = True
                for i in range(lo, hi):
                    if less(nums[i + 1], nums[i]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        this_turn_not_exchanged = False
                if this_turn_not_exchanged:
                    break
                hi -= 1

                this_turn_not_exchanged = True
                for i in reversed(range(lo + 1, hi + 1)):
                    if less(nums[i], nums[i - 1]):
                        nums[i], nums[i - 1] = nums[i - 1], nums[i]
                        this_turn_not_exchanged = False
                if this_turn_not_exchanged:
                    break
                lo += 1
            return nums

        # n2, 不稳定
        def select_sort(nums):
            for pos in reversed(range(1, len(nums))):
                imax = 0
                for i in range(pos + 1):
                    if less(nums[imax], nums[i]):
                        imax = i
                nums[imax], nums[pos] = nums[pos], nums[imax]
            return nums

        # n2, 稳定
        def insert_sort(nums):
            for i in range(1, len(nums)):
                temp = nums[i]
                j = i
                while j - 1 >= 0 and less(temp, nums[j - 1]):
                    nums[j] = nums[j - 1]
                    j -= 1
                nums[j] = temp
            return nums

        # nlogn*logn, 不稳
        # 插入排序的改进: 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率, 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
        # 根据步长将数组分成n组, nums[i::n], 对这些子数组排序, 然后逐渐减少步长, 步长为1时, 数组为原数组
        def shell_sort(nums):
            gap = len(nums) // 2  # 初始步長
            while gap > 0:
                for i in range(gap, len(nums)):
                    temp = nums[i]
                    j = i
                    while j - gap >= 0 and less(temp, nums[j - gap]):
                        nums[j] = nums[j - gap]
                        j -= gap
                    nums[j] = temp
                # 得到新的步長
                gap = gap // 2
            return nums

        # nlogn, 稳
        def merge_sort(nums):
            # 全局变量暂存需要归并的数组
            temp = [0] * len(nums)

            # 原地归并
            def merge(a, lo, mid, hi):
                for k in range(lo, hi + 1):
                    temp[k] = a[k]
                i, j = lo, mid + 1
                for k in range(lo, hi + 1):
                    if i > mid:  # 左半边没了
                        a[k] = temp[j]
                        j += 1
                    elif j > hi:  # 右半边没了
                        a[k] = temp[i]
                        i += 1
                    elif less(temp[j], temp[i]):
                        a[k] = temp[j]
                        j += 1
                    else:
                        a[k] = temp[i]
                        i += 1

            def sort(a, lo, hi):
                if lo >= hi:
                    return
                mid = lo + (hi - lo) // 2
                sort(a, lo, mid)
                sort(a, mid + 1, hi)
                merge(a, lo, mid, hi)

            sort(nums, 0, len(nums) - 1)
            return nums

        # nlogn, 不稳
        def quick_sort(nums):
            # TLE
            def partition1(a, lo, hi):
                v = a[lo]
                while lo < hi:
                    while lo < hi and not less(a[hi], v):
                        hi -= 1
                    a[lo] = a[hi]
                    while lo < hi and less(a[lo], v):
                        lo += 1
                    a[hi] = a[lo]
                a[lo] = v
                return lo

            # TLE
            def partition2(a, lo, hi):
                v = a[hi]
                p = lo
                for i in range(lo, hi):  # hi 不比较
                    if less(a[i], v):
                        a[i], a[p], a[p], a[i]
                        p += 1
                # nums[:p]   <  v
                # nums[p:hi] >= v
                # nums[hi]   == v
                # 所以交换 p 和 hi
                a[p], a[hi] = a[hi], a[p]
                return p

            # TLE
            def partition3(a, lo, hi):
                v = a[lo]
                p = lo
                for i in range(lo + 1, hi + 1):  # lo 不比较
                    if less(a[i], v):
                        p += 1
                        a[i], a[p] = a[p], a[i]
                # nums[lo]    ==  v
                # nums[1:p]   <   v
                # nums[p+1:]  >=  v
                # 所以交换 p 和 lo
                a[p], a[lo] = a[lo], a[p]
                return p

            # 双路partition
            # 对于 partition123, 如果有大量相等的 pivot, 都会被分到同一边
            # 极端情况下, 快排退化成O2
            def partition4(a, lo, hi):
                v = a[lo]
                l, r = lo + 1, hi  # 不比较 lo
                while 1:
                    # l 从左到右找到第一个 >= v 的索引为 l, 把 < v 的留在左边
                    while l <= hi and less(a[l], v):
                        l += 1
                    # l 从右到左找到第一个 <= v 的索引为 r, 把 > v 的留在右边
                    while r >= lo + 1 and less(v, a[r]):
                        r -= 1
                    # 说明已经移动完了
                    if l > r:
                        break
                    # 交换, 移动, 交换后, r 右边都是 >= v, l 左边都是 <= v
                    # 也就是说如果有等于v的数据会被平衡分到两边
                    a[l], a[r] = a[r], a[l]
                    l += 1
                    r -= 1
                    # nums[:l]   都 <= v
                    # nums[r+1:] 都 >= v
                # 因为 a[r] <= v 且 a[r+1:] > v
                a[lo], a[r] = a[r], a[lo]
                return r

            # 三路partition
            def partition5(a, lo, hi):
                v = a[lo]
                l, i, r = lo, lo + 1, hi
                while i <= r:
                    if less(a[i], v):  # a[lo...l-1] < v
                        a[l], a[i] = a[i], a[l]
                        l += 1
                        i += 1
                    elif less(v, a[i]):  # a[r+1...hi] > v
                        a[i], a[r] = a[r], a[i]
                        r -= 1
                    else:  # a[l...r] = v
                        i += 1
                return l, r

            partition = partition5

            def random_partition(a, lo, hi):
                p = random.randint(lo, hi)
                a[lo], a[p] = a[p], a[lo]
                return partition(a, lo, hi)

            def sort(a, lo, hi):
                if lo >= hi:
                    return
                p = random_partition(a, lo, hi)
                if isinstance(p, int):
                    sort(a, lo, p - 1)
                    sort(a, p + 1, hi)
                else:
                    l, r = p
                    sort(a, lo, l - 1)
                    sort(a, r + 1, hi)

            sort(nums, 0, len(nums) - 1)

            return nums

        # nlogn, 不稳
        # 最大堆, 依次把堆顶元素放到最后面就是递增序列
        def heap_sort(nums):
            # 元素向上调整, 不断和父节点比较
            def shift_up(h, i):
                f = (i - 1) // 2
                if f >= 0 and less(h[f], h[i]):
                    h[i], h[f] = h[f], h[i]
                    shift_up(h, f)

            # 元素向下调整, 不断和两个子节点比较
            def shift_down(h, i, bound=None):
                if bound is None:
                    bound = len(h)
                f, l, r = i, i * 2 + 1, i * 2 + 2
                # f 是 父节点和两个子节点中的最大
                if l < bound and less(h[f], h[l]):
                    f = l
                if r < bound and less(h[f], h[r]):
                    f = r
                if f != i:
                    h[i], h[f] = h[f], h[i]
                    shift_down(h, f, bound)

            def heap_push(h, v):
                h.append(v)
                shift_up(h, len(h) - 1)

            def heap_pop(h):
                if not h:
                    raise IndexError
                h[0], h[-1] = h[-1], h[0]
                v = h.pop()
                shift_down(h, 0)
                return v

            def build_heap(a):
                for i in reversed(range(len(a) // 2)):
                    shift_down(a, i)

            def sort(a):
                build_heap(a)
                for i in reversed(range(len(a))):
                    a[0], a[i] = a[i], a[0]
                    shift_down(a, 0, i)
                return a

            sort(nums)

            return nums

        # n, 不稳, 只适用于重复较多范围较小的整数数组
        def count_sort(nums):
            min_value, max_value = min(nums), max(nums)
            buckets = [0] * (max_value - min_value + 1)
            for num in nums:
                buckets[num - min_value] += 1
            idx = 0
            for bucket_index, count in enumerate(buckets):
                for _ in range(count):
                    nums[idx] = bucket_index + min_value
                    idx += 1
            return nums

        # count_sort 的改进版本
        def bucket_sort(nums):
            def toBucket(num, bs=50):  # 映射到连续的桶中, 不同的桶中的元素大小已经确定
                return num // bs

            min_value, max_value = min(nums), max(nums)
            buckets = [[] for _ in range(toBucket(max_value - min_value) + 1)]
            for num in nums:
                buckets[toBucket(num - min_value)].append(num)
            res = []
            for bucket in buckets:
                res.extend(sorted(bucket))
            return res

        # 基数排序, 也可以用来对字符串数组排序
        def radix_sort(nums, base=10):
            min_value, max_value = min(nums), max(nums)
            # 找出列表中最大的位数
            max_digit = 1
            while base**max_digit <= max_value - min_value:  # 减最小值主要为了处理负数
                max_digit = max_digit + 1

            # 从低到高求位值排序, 最低位从0开始记
            for digit in range(max_digit):
                buckets = [[] for _ in range(base)]
                for num in nums:
                    t = ((num - min_value) // base**digit) % base
                    buckets[t].append(num)

                nums = []
                for bucket in buckets:
                    nums.extend(bucket)

            return nums

        return heap_sort(nums)


# @lc code=end
# import random

# x = [random.randint(0, 100) for _ in range(10000)]
# y = sorted(x)
# print(Solution().sortArray(x) == y)
