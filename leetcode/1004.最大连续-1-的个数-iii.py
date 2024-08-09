# @lc app=leetcode.cn id=1004 lang=python3
# [1004] 最大连续1的个数 III
# https://leetcode.cn/problems/max-consecutive-ones-iii/description/
# Medium (59.31%)
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
# 示例 1：
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 示例 2：
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
# 提示：
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1
# 0 <= k <= nums.length

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        while right < len(nums):
            # 右进
            if nums[right] == 1:
                right += 1
            else:
                if k > 0:
                    right += 1
                    k -= 1
                else:
                    res = max(res, right - left)
                    # 左出
                    while k == 0:
                        if nums[left] == 0:
                            k += 1
                        left += 1
        res = max(res, right - left)
        return res
# @lc code=end
