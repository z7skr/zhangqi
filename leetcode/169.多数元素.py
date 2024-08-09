# @lc app=leetcode.cn id=169 lang=python3
# [169] 多数元素
# https://leetcode.cn/problems/majority-element/description/
# Easy (66.33%)
# Testcase Example:  '[3,2,3]'
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1：
# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
# 提示：
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。


# @lc code=start
class Solution:
    from typing import List

    def majorityElement(self, nums: List[int]) -> int:
        def partition():
            pass

        def bf():
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
                if counts[num] > len(nums) // 2:
                    return num

        def best():
            ans, count = nums[0], 0
            for num in nums:
                if count == 0:  # 被其他元素抵消完了就换新的ans
                    ans = num
                    count += 1
                elif num == ans:
                    count += 1
                else:  # 不相等就抵消
                    count -= 1
            return ans

        return best()


# @lc code=end


func = Solution().majorityElement
nums = [3, 2, 3]
print(func(nums))
# 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(func(nums))
# 2
