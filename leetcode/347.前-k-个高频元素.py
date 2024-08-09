# @lc app=leetcode.cn id=347 lang=python3
# [347] 前 K 个高频元素
# https://leetcode.cn/problems/top-k-frequent-elements/description/
# Medium (63.62%)
# Testcase Example:  '[1,1,1,2,2,3]\n2'
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]
# 提示：
# 1
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。


# @lc code=start
from collections import Counter
import heapq


class Solution:
    from typing import List

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def brutal():
            return [i for i, _ in Counter(nums).most_common(k)]

        def priority_q():
            count_map = {}
            for num in nums:
                count_map[num] = count_map.get(num, 0) + 1
            count_list = [[-v, kk] for kk, v in count_map.items()]
            heapq.heapify(count_list)
            res = []
            for _ in range(k):
                res.append(heapq.heappop(count_list)[1])
            return res

        return priority_q()


# @lc code=end


func = Solution().topKFrequent
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(func(nums, k))
#  [1,2]

nums = [1]
k = 1
print(func(nums, k))
#  [1]
