# @lc app=leetcode.cn id=207 lang=python3
# [207] 课程表
# https://leetcode.cn/problems/course-schedule/description/
# Medium (53.91%)
# Testcase Example:  '2\n[[1,0]]'
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
# 提示：
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同


# @lc code=start
from collections import deque
import grp


class Solution:
    from typing import List

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def make_graph_and_indegree():
            graph = [[] for _ in range(numCourses)]
            indeg = [0 for _ in range(numCourses)]
            for t, f in prerequisites:
                graph[f].append(t)
                indeg[t] += 1
            return graph, indeg

        def dfs():
            graph, _ = make_graph_and_indegree()
            visited = [False] * numCourses
            on_path = [False] * numCourses
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

            for i in range(numCourses):
                dfs(i)
            return not has_cycle

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
            return len(path) == numCourses

        return dfs()


# @lc code=end


func = Solution().canFinish
numCourses = 2
prerequisites = [[1, 0]]
print(func(numCourses, prerequisites))
# true
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(func(numCourses, prerequisites))
# false
numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
print(func(numCourses, prerequisites))
# false
numCourses = 3
prerequisites = [[2, 1], [2, 0], [1, 0]]
print(func(numCourses, prerequisites))
# true
