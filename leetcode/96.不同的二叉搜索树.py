# @lc app=leetcode.cn id=96 lang=python3
# [96] 不同的二叉搜索树
# https://leetcode.cn/problems/unique-binary-search-trees/description/
# Medium (70.86%)
# Testcase Example:  '3'
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 示例 1：
# 输入：n = 3
# 输出：5
# 示例 2：
# 输入：n = 1
# 输出：1

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        memo = [1] * (n + 1)
        for i in range(1, n + 1):
            memo[i] = sum([memo[j] * memo[i-1-j] for j in range(i)])
        return memo[n]
# @lc code=end
