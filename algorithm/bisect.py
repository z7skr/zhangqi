def search(a, k):
    # [1,2,2,2,3,...], 2 --> 1,2,3都可能
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < k:  # [lo, hi]
            lo = mid + 1
        elif a[mid] > k:
            hi = mid - 1
        else:
            return mid
    return -1


def search_left(a, k):
    # [1,2,2,2,3], 2 --> 1
    if len(nums) == 0:
        return -1
    lo, hi = 0, len(a)
    while lo < hi:  # [lo, hi)
        mid = lo + (hi - lo) // 2
        if a[mid] < k:
            lo = mid + 1
        else:
            hi = mid
    return lo if nums[lo] == target else -1


def search_right(nums, k):
    # [1,2,2,2,3], 2 --> 3
    if len(nums) == 0:
        return -1
    lo, hi = 0, len(nums)
    while lo < hi:  # [lo, hi)
        mid = (lo + hi) // 2
        if nums[mid] > k:
            hi = mid
        else:
            lo = mid + 1
    return hi - 1 if nums[hi - 1] == target else -1


nums = [-1, 0, 3, 3, 3, 5, 9, 12]
target = 3
print(search_right(nums, target))
