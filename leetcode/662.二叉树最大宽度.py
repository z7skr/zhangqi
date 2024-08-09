# @lc app=leetcode.cn id=662 lang=python3
# [662] 二叉树最大宽度
# https://leetcode.cn/problems/maximum-width-of-binary-tree/description/
# Medium (43.78%)
# Testcase Example:  '[1,3,2,5,3,null,9]'
# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
# 树的 最大宽度 是所有层中最大的 宽度 。
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null
# 节点，这些 null 节点也计入长度。
# 题目数据保证答案将会在  32 位 带符号整数范围内。
# 示例 1：
# 输入：root = [1,3,2,5,3,null,9]
# 输出：4
# 解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。
# 示例 2：
# 输入：root = [1,3,2,5,null,null,9,6,null,7]
# 输出：7
# 解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。
# 示例 3：
# 输入：root = [1,3,2,5]
# 输出：2
# 解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。
# 提示：
# 树中节点的数目范围是 [1, 3000]
# -100 <= Node.val <= 100


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from typing import Optional

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def dfs():
            def dfs(node, level, column):
                if not node:
                    return
                di[level] = di.get(level, []) + [column]
                dfs(node.left, level + 1, column * 2)
                dfs(node.right, level + 1, column * 2 + 1)

            di = {}
            dfs(root, 0, 0)
            return max(max(di[level]) - min(di[level]) + 1 for level in di)

        return dfs()


# @lc code=end

func = Solution().widthOfBinaryTree
root = TreeNode(
    1,
    left=TreeNode(3, left=TreeNode(5, left=TreeNode(6))),
    right=TreeNode(2, right=TreeNode(9, left=TreeNode(7))),
)
print(func(root))
