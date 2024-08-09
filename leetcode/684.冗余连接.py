# @lc app=leetcode.cn id=684 lang=python3
# [684] 冗余连接
# https://leetcode.cn/problems/redundant-connection/description/
# Medium (67.66%)
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
# 树可以看成是一个连通且 无环 的 无向 图。
# 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n
# 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和
# bi 之间存在一条边。
# 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的那个。
# 示例 1：
# 输入: edges = [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 示例 2：
# 输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
# 提示:
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# edges 中无重复元素
# 给定的图是连通的


# @lc code=start
class Solution:
    from typing import List

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def union_find():
            # 初始化: 每个连通分量都指向自己
            parent = [i for i in range(len(edges) + 1)]

            # find & 路径压缩
            def find(x: int) -> int:
                if x != parent[x]:
                    parent[x] = find(parent[x])  # 相当于一个后序遍历压缩路径
                return parent[x]

            # 连通两个点: 将 [一个点的祖先] 的 parent 设置为 [另一个点的祖先]
            def union(x: int, y: int) -> None:
                parent[find(x)] = find(y)

            # 对每条直接连接的边, 如果仍然是间接连通的, 说明有环
            # 因为只需要去掉一条边就不多余了, 所以按顺序遍历的得到的就是最后一条多余的边
            for a, b in edges:
                if find(a) == find(b):
                    return [a, b]
                else:
                    union(a, b)

            return []

        return union_find()


# @lc code=end

func = Solution().findRedundantConnection

edges = [[1, 2], [1, 3], [2, 3]]
print(func(edges))
# 输出: [2,3]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(func(edges))
# 输出: [1,4]


def find1(x: int) -> int:
    if x != parent[x]:
        parent[x] = find1(parent[x])
    return parent[x]


def find2(x: int) -> int:
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


parent = [i + 1 for i in range(21)]
parent[20] = 20
print(parent)
find1(0)
print(parent)
parent = [i + 1 for i in range(21)]
parent[20] = 20
find2(0)
print(parent)
