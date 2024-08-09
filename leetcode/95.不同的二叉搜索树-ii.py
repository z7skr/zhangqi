# @lc app=leetcode.cn id=95 lang=python3
# [95] 不同的二叉搜索树 II
# https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
# Medium (73.23%)
# Testcase Example:  '3'
# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
# 示例 1：
# 输入：n = 3
# 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 示例 2：
# 输入：n = 1
# 输出：[[1]]
# 提示：
# 1

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  # Definition for a binary tree node.


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTrees_递归(n)

    def generateTrees_递归(self, n: int) -> List[Optional[TreeNode]]:
        def generate(nums):
            if not nums:
                return [None]  # list
            res = []
            for n in nums:  # 每个数字都可以是根节点
                # 根据定义得到, 左右所有的子树
                lefts = generate([i for i in nums if i < n])
                rights = generate([i for i in nums if i > n])
                # 组合起来, 根节点+左右节点
                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(n, left=l, right=r))
            return res

        return generate(list(range(1, n + 1)))


# @lc code=end
