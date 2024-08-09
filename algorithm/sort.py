# n2, 稳定
def bubble_sort(nums):
    for turn in range(1, len(nums)):
        exchanged = False
        for i in range(len(nums) - turn):
            if nums[i + 1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                exchanged = True
        if not exchanged:
            break
    return nums


# n2
def bidirectinal_bubble_sort(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        this_turn_not_exchanged = True
        for i in range(lo, hi):
            if nums[i + 1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                this_turn_not_exchanged = False
        if this_turn_not_exchanged:
            break
        hi -= 1

        this_turn_not_exchanged = True
        for i in reversed(range(lo + 1, hi + 1)):
            if nums[i] < nums[i - 1]:
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
            if nums[imax] < nums[i]:
                imax = i
        nums[imax], nums[pos] = nums[pos], nums[imax]
    return nums


# n2, 稳定
def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while j - 1 >= 0 and temp < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp
    return nums


# nlogn, logn, 不稳
# 插入排序的改进: 插入排序在对几乎已经排好序的数据操作时，效率高，基本达到线性排序的效率
# 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
# 根据步长将数组分成n组, nums[i::n], 对这些子数组排序, 然后逐渐减少步长, 步长为1时, 数组为原数组
def shell_sort(nums):
    gap = len(nums) // 2  # 初始步長
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i
            while j - gap >= 0 and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap // 2  # 得到新的步長
    return nums


# nlogn, 稳
def merge_sort(nums):
    # 全局变量暂存需要归并的数组
    temp = [0] * len(nums)

    # 原地归并
    def merge(a, lo, mid, hi):
        for k in range(lo, hi + 1):
            temp[k] = a[k]
        left, right = lo, mid + 1
        for k in range(lo, hi + 1):
            if left > mid:
                a[k] = temp[right]
                right += 1
            elif right > hi:
                a[k] = temp[left]
                left += 1
            elif temp[left] < temp[right]:
                a[k] = temp[left]
                left += 1
            else:
                a[k] = temp[right]
                right += 1

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
            while lo < hi and a[hi] >= v:
                hi -= 1
            a[lo] = a[hi]
            while lo < hi and a[lo] < v:
                lo += 1
            a[hi] = a[lo]
        a[lo] = v
        return lo

    # TLE
    def partition2(a, lo, hi):
        v = a[lo]
        p = lo
        for i in range(lo + 1, hi + 1):  # lo 不比较
            if a[i] < v:
                p += 1  # 先+1
                a[i], a[p] = a[p], a[i]
        # nums[lo] == v, nums[lo+1:p+1] < v, nums[p+1:hi+1] >=  v
        # 所以交换 p 和 lo
        a[p], a[lo] = a[lo], a[p]
        return p

    # 双路partition
    # 对于 partition123, 如果有大量相等的 pivot, 都会被分到同一边, 极端情况下, 快排退化成O2
    def partition3(a, lo, hi):
        v = a[lo]
        l, r = lo + 1, hi  # 不比较 lo
        while 1:
            while l <= hi and a[l] < v:
                l += 1  # a[l] 是左边第一个 >= v 的
            while r >= lo and a[r] > v:
                r -= 1  # a[r] 是右边第一个 <= v 的
            if l >= r:  # 说明已经移动完了
                break
            a[l], a[r] = a[r], a[l]  # r右 >= v, l左 <= v, 等于v的数据会被平衡分到两边
            l, r = l + 1, r - 1
        a[lo], a[r] = a[r], a[lo]  # a[r] 是右边第一个 <= v 的
        return r

    # 三路partition
    def partition4(a, lo, hi):
        v = a[lo]
        l, i, r = lo, lo + 1, hi
        while i <= r:
            if a[i] < v:  # a[lo...l-1] < v
                a[l], a[i] = a[i], a[l]
                l += 1
                i += 1
            elif a[i] > v:  # a[r+1...hi] > v
                a[i], a[r] = a[r], a[i]
                r -= 1
            else:  # a[l...r] = v
                i += 1
        return l, r

    partition = partition4

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
        else:  # 三路partition的返回
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
        if f >= 0 and h[f] < h[i]:
            h[i], h[f] = h[f], h[i]
            shift_up(h, f)

    # 元素向下调整, 不断和两个子节点比较
    def shift_down(h, i, bound=None):
        f, l, r = i, 2 * i + 1, 2 * i + 2
        # f 是 父节点和两个子节点中的最大
        if bound is None:
            bound = len(h)
        if l < bound and h[f] < h[l]:
            f = l
        if r < bound and h[f] < h[r]:
            f = r
        if f != i:
            h[i], h[f] = h[f], h[i]
            shift_down(h, f, bound)

    def heapify(a):
        for i in reversed(range(len(a) // 2)):
            shift_down(a, i)

    def heappush(h, v):
        h.append(v)
        shift_up(h, len(h) - 1)

    def heappop(h):
        if not h:
            raise IndexError
        h[0], h[-1] = h[-1], h[0]
        v = h.pop()
        shift_down(h, 0)
        return v

    def sort(a):
        heapify(a)
        for i in reversed(range(len(a))):
            a[0], a[i] = a[i], a[0]
            shift_down(a, 0, i)

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


import random

x = [random.randint(0, 10) for _ in range(20)]
y = sorted(x)
print(quick_sort(x) == y)
