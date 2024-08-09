# @lc app=leetcode.cn id=219 lang=python3
# [219] 存在重复元素 II
# https://leetcode.cn/problems/contains-duplicate-ii/description/
# Easy (45.52%)
# Testcase Example:  '[1,2,3,1]\n3'
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 示例 2：
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 示例 3：
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
# 提示：
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        def f1(nums, k):
            window = set()
            for i in range(min(k+1, len(nums))):
                n = nums[i]
                if n in window:
                    return True
                window.add(n)
            for i in range(k+1, len(nums)):
                n = nums[i-k-1]
                window.remove(n)
                n = nums[i]
                if n in window:
                    return True
                window.add(n)
            return False

        def f2(nums, k):
            window = set()
            left, right = 0, 0
            # 右进
            while right < len(nums):
                n = nums[right]
                right += 1

                if n in window:
                    return True
                window.add(n)
                # 左出
                while right - left > k:
                    n = nums[left]
                    left += 1
                    window.remove(n)

            return False


        return f2(nums, k)


# @lc code=end
