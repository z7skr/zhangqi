# @lc app=leetcode.cn id=210 lang=python3
# [210] 课程表 II
# https://leetcode.cn/problems/course-schedule-ii/description/
# Medium (57.86%)
# Testcase Example:  '2\n[[1,0]]'
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中
# prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2：
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 示例 3：
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
# 提示：
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# 所有[ai, bi] 互不相同


# @lc code=start

from collections import deque


class Solution:
    from typing import List

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def make_graph_and_indegree():
            graph = [[] for _ in range(numCourses)]
            indeg = [0 for _ in range(numCourses)]
            for t, f in prerequisites:
                graph[f].append(t)
                indeg[t] += 1
            return graph, indeg

        def dfs():
            # 后序遍历: 等所有子节点都遍历完了再遍历当前节点
            graph, _ = make_graph_and_indegree()
            visited = [False] * numCourses
            on_path = [False] * numCourses
            postorder = []
            has_cycle = False

            def dfs(i):
                nonlocal has_cycle
                if on_path[i]:
                    has_cycle = True
                if visited[i] or has_cycle:
                    return
                visited[i] = True
                on_path[i] = True
                for j in graph[i]:
                    dfs(j)
                on_path[i] = False
                # 后序遍历
                postorder.append(i)

            for i in range(numCourses):
                dfs(i)
            return [] if has_cycle else postorder[::-1]

        def bfs():
            graph, indeg = make_graph_and_indegree()
            q = deque([i for i in range(numCourses) if indeg[i] == 0])
            path = []
            while q:
                size = len(q)
                for _ in range(size):
                    c = q.popleft()
                    path.append(c)
                    for i in graph[c]:
                        indeg[i] -= 1
                        if indeg[i] == 0:
                            q.append(i)
            return path if len(path) == numCourses else []

        return dfs()


# @lc code=end


func = Solution().findOrder
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(func(numCourses, prerequisites))
# [0,1,2,3]
numCourses = 2
prerequisites = [[1, 0]]
print(func(numCourses, prerequisites))
# [0,1]
numCourses = 1
prerequisites = []
print(func(numCourses, prerequisites))
# [0]
numCourses = 3
prerequisites = [[1, 0], [2, 0]]
print(func(numCourses, prerequisites))
# [0,2,1]
