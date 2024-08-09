# @lc app=leetcode.cn id=752 lang=python3
# [752] 打开转盘锁
# https://leetcode.cn/problems/open-the-lock/description/
# Medium (52.78%)
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
# 示例 1:
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 示例 2:
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 示例 3:
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
# 提示：
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs1(deadends: List[str], target: str) -> int:
            q, q_tmp = deque(["0000"]), set()
            visited = set()
            res = -1
            while q:
                res += 1
                size = len(q)
                for _ in range(size):
                    c = q.popleft()
                    if c in deadends:  # 出队的时候再访问
                        continue
                    if c in visited:
                        continue
                    visited.add(c)
                    if c == target:
                        return res
                    for i in range(4):
                        for j in [1, -1]:
                            x = chr((ord(c[i]) - ord("0") + 10 + j) % 10 + ord("0"))
                            d = c[:i] + x + c[i + 1 :]
                            q_tmp.add(d)
                q.extend(list(q_tmp))
                q_tmp.clear()
            return -1

        def bfs2(deadends, target) -> int:
            q, q_tmp = deque(["0000"]), set()
            visited = set(["0000"])
            res = -1
            while q:
                res += 1
                size = len(q)
                for _ in range(size):
                    c = q.popleft()
                    if c in deadends:
                        continue
                    if c == target:
                        return res
                    for i in range(4):
                        for j in [1, -1]:
                            x = chr((ord(c[i]) - ord("0") + 10 + j) % 10 + ord("0"))
                            d = c[:i] + x + c[i + 1 :]
                            if d in visited:
                                continue
                            visited.add(d)  # 进队的时候就访问
                            q_tmp.add(d)
                q.extend(list(q_tmp))
                q_tmp.clear()
            return -1

        return bfs1(deadends, target)


# @lc code=end
f = Solution().openLock
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
print(f(deadends, target))
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(f(deadends, target))
deadends = ["0000"]
target = "8888"
print(f(deadends, target))
