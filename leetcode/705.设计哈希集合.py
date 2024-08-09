# @lc app=leetcode.cn id=705 lang=python3
# [705] 设计哈希集合
# https://leetcode.cn/problems/design-hashset/description/
# Easy (63.50%)
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +'[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 示例：
# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]
# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除）
# 提示：
# 0 <= key <= 10^6
# 最多调用 10^4 次 add、remove 和 contains


# @lc code=start
class MyHashSet:

    def __init__(self):
        self.d = 107
        self.a = [[] for _ in range(self.d)]

    def hash(self, key):
        return key % self.d

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.a[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.a[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.a[self.hash(key)]


myHashSet = MyHashSet()
myHashSet.add(1)  # set = [1]
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(1))  # 返回 True
print(myHashSet.contains(3))  # 返回 False ，（未找到）
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(2))  # 返回 True
myHashSet.remove(2)  # set = [1]
print(myHashSet.contains(2))  # 返回 False ，（已移除）
