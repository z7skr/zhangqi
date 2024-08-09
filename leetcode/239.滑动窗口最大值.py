# @lc app=leetcode.cn id=239 lang=python3
# [239] 滑动窗口最大值
# https://leetcode.cn/problems/sliding-window-maximum/description/
# Hard (49.07%)
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
# 示例 1：
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
# 输入：nums = [1], k = 1
# 输出：[1]
# 提示：
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()  # index 的队列
        res = []
        for i, cur in enumerate(nums):
            # 维护window递减, 把window最右边比cur小的都pop掉, 因为cur进来后这些元素都用不到了
            while window and nums[window[-1]] <= cur:
                window.pop()
            window.append(i)
            # remove from window
            if window[0] == i - k:
                window.popleft()
            # cur出window时window内的元素都是递减的, 第一个就是最大值
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


# @lc code=end
