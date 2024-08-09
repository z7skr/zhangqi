# @lc app=leetcode.cn id=77 lang=python3
# [77] 组合
# https://leetcode.cn/problems/combinations/description/
# Medium (77.03%)
# Testcase Example:  '4\n2'
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 示例 2：
# 输入：n = 1, k = 1
# 输出：[[1]]
# 提示：
# 1
# 1

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs1(n, k):
            def dfs(i, path):
                # if i == n:
                #     return
                if len(path) + n - i < k:
                    return
                if len(path) == k:
                    res.append(path)  # 值传递, 不需要 copy
                    return
                dfs(i + 1, path + [i + 1])
                dfs(i + 1, path + [])

            res = []
            dfs(0, [])
            return res

        def dfs2(n, k):
            def dfs(i):
                # if i == n:
                #     return
                if len(path) + n - i < k:
                    return
                if len(path) == k:
                    res.append(path[:])
                    return
                path.append(i + 1)
                dfs(i + 1)
                path.pop()
                dfs(i + 1)

            res, path = [], []
            dfs(0)
            return res

        def dfs3(n, k):
            def dfs(nex):
                # next, 可以选择的最小数字
                if len(path) == k:
                    res.append(path[:])
                    return
                # 对可以选择的所有数, 一个一个选, 选了之后可以选择的最小数字就是 i+1 了
                # 第一个选了之后撤销, 再选第二个, 此时第一个就是没选
                for i in range(nex, n + 1):
                    path.append(i)
                    dfs(i + 1)
                    path.pop()

            res, path = [], []
            dfs(1)
            return res

        return dfs3(n, k)


# @lc code=end
n = 4
k = 2
print(Solution().combine(n, k))
