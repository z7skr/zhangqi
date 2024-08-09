# @lc app=leetcode.cn id=685 lang=python3
# [685] 冗余连接 II
# https://leetcode.cn/problems/redundant-connection-ii/description/
# Hard (42.28%)
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
# 在本问题中，有根树指满足以下条件的有向图。
# 该树只有一个根节点，所有其他节点都是该根节点的后继。
# 该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
# 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n
# 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
# 结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是
# vi 的一个父节点。
# 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
# 示例 1：
# 输入：edges = [[1,2],[1,3],[2,3]]
# 输出：[2,3]
# 示例 2：
# 输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# 输出：[4,1]
# 提示：
# n == edges.length
# 3
# edges[i].length == 2
# 1 i, vi


# @lc code=start
class Solution:
    from typing import List

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def union_find():
            parent = [i for i in range(len(edges) + 1)]

            def find(x: int) -> int:
                if x != parent[x]:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x: int, y: int) -> None:
                parent[find(y)] = find(x)

            for x, y in edges:
                if find(x) == find(y):
                    return [x, y]
                else:
                    union(x, y)

            return []

        return union_find()


# @lc code=end

func = Solution().findRedundantDirectedConnection
edges = [[1, 2], [1, 3], [2, 3]]
print(func(edges))
# [2,3]
edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
print(func(edges))
# [4,1]
edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
print(func(edges))
# [2,1]
