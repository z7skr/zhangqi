# @lc app=leetcode.cn id=4 lang=python3
# [4] 寻找两个正序数组的中位数
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
# Hard (41.54%)
# Testcase Example:  '[1,3]\n[2]'
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 提示：
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def brute_force(a, b):
            i, j = 0, 0
            nums = []
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    nums.append(a[i])
                    i += 1
                else:
                    nums.append(b[j])
                    j += 1
            nums += a[i:] + b[j:]
            L = len(nums)
            return (nums[L // 2] + nums[(L - 1) // 2]) / 2

        def find_median():
            def kth(a, b, k):
                if not a:
                    return b[k]
                if not b:
                    return a[k]
                ia, ib = len(a) // 2, len(b) // 2
                ai, bi = a[ia], b[ib]
                if k > ia + ib:
                    if ai > bi:  # ai >= a[:ia+1],b[:ib+1]
                        return kth(a, b[ib + 1 :], k - ib - 1)
                    else:  # bi >= a[:ia+1],b[:ib+1]
                        return kth(a[ia + 1 :], b, k - ia - 1)
                else:
                    if ai > bi:
                        return kth(a[:ia], b, k)
                    else:
                        return kth(a, b[:ib], k)

            L = len(nums1) + len(nums2)
            if L % 2 == 0:
                return (kth(nums1, nums2, (L - 1) // 2) + kth(nums1, nums2, L // 2)) / 2
            else:
                return kth(nums1, nums2, L // 2)

        def find_center():
            def kth(a, b, k):
                if not a:
                    return b[k]
                if not b:
                    return a[k]
                ia, ib = len(a) // 2, len(b) // 2
                ai, bi = a[ia], b[ib]
                if k > ia + ib:
                    if ai > bi:
                        return kth(a, b[ib + 1 :], k - ib - 1)
                    else:
                        return kth(a[ia + 1 :], b, k - ia - 1)
                else:
                    if ai > bi:
                        return kth(a[:ia], b, k)
                    else:
                        return kth(a, b[:ib], k)

            L = len(nums1) + len(nums2)
            return (kth(nums1, nums2, (L - 1) // 2) + kth(nums1, nums2, L // 2)) / 2

        return find_center()


# @lc code=end
func = Solution().findMedianSortedArrays

nums1 = [1, 3]
nums2 = [2]
print(func(nums1, nums2))
# 输出：2.00000

nums1 = [1, 2]
nums2 = [3, 4]
print(func(nums1, nums2))
# 输出：2.50000
