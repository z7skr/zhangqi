# @lc app=leetcode.cn id=473 lang=python3
# [473] 火柴拼正方形
# htedge_tuple://leetcode.cn/problems/matchedges-to-square/description/
# Medium (46.70%)
# Testcase Example:  '[1,1,2,2,2]'
# 你将得到一个整数数组 matchedges ，其中 matchedges[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你
# 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
# 如果你能使这个正方形，则返回 true ，否则返回 false 。
# 示例 1:
# 输入: matchedges = [1,1,2,2,2]
# 输出: true
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例 2:
# 输入: matchedges = [3,3,3,3,4]
# 输出: false
# 解释: 不能用所有火柴拼成一个正方形。
# 提示:
# 1 <= matchedges.length <= 15
# 1 <= matchedges[i] <= 10^8


# @lc code=start
from typing import List


class Solution:

    def makesquare(self, matchedges: List[int]) -> bool:
        def dfs1():
            def dfs(n, i, curlen):  # n: 还剩几条边, i: 遍历序号, curlen: 当前边长度和
                if n == 0:
                    return True
                if i == len(edge_counter):
                    return False
                res = False
                for k in range(edge_tuple[i][1] + 1):  # 选择 k 个 edge
                    if curlen + edge_tuple[i][0] * k < target:
                        edge_tuple[i][1] -= k
                        res = res or dfs(n, i + 1, curlen + edge_tuple[i][0] * k)
                        edge_tuple[i][1] += k
                    elif curlen + edge_tuple[i][0] * k == target:
                        edge_tuple[i][1] -= k
                        res = res or dfs(n - 1, 0, 0)
                        edge_tuple[i][1] += k
                return res

            edge_counter = {}
            for l in matchedges:
                edge_counter[l] = edge_counter.get(l, 0) + 1
            edge_tuple = [[k, v] for k, v in edge_counter.items()]
            # k 是 edge 长度, v 是 edge 数量
            return dfs(4, 0, 0)

        def dfs2():
            def dfs(l1, l2, l3, l4, i):
                if l1 == l2 == l3 == l4 == target:
                    return True
                if i == len(matchedges):
                    return False
                if l1 > target or l2 > target or l3 > target or l4 > target:
                    return False
                return (
                    dfs(l1 + matchedges[i], l2, l3, l4, i + 1)
                    or dfs(l1, l2 + matchedges[i], l3, l4, i + 1)
                    or dfs(l1, l2, l3 + matchedges[i], l4, i + 1)
                    or dfs(l1, l2, l3, l4 + matchedges[i], i + 1)
                )

            matchedges.sort(reverse=True)
            return dfs(0, 0, 0, 0, 0)

        SUM = sum(matchedges)
        if SUM & 3 != 0:
            return False
        target = SUM >> 2
        if max(matchedges) > target:
            return False
        return dfs1()


# @lc code=end


func = Solution().makesquare
matchedges = [1, 1, 2, 2, 2]
print(func(matchedges))
#  true

matchedges = [3, 3, 3, 3, 4]
print(func(matchedges))
#  false

matchedges = [5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4]
print(func(matchedges))
#  false
