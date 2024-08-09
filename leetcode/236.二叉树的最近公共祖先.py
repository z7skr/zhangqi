# @lc app=leetcode.cn id=236 lang=python3
# [236] 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Medium (71.49%)
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
# 提示：
# 树中节点数目在范围 [2, 10^5] 内。
# -10^9
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def preorder():
            path, path_p, path_q = [], [], []

            def traverse(head):
                if not head or path_p and path_q:
                    return
                path.append(head)  # 先写
                if head == p:
                    path_p.extend(path)
                elif head == q:
                    path_q.extend(path)
                traverse(head.left)
                traverse(head.right)
                path.pop()  # 后出

            traverse(root)
            res = None
            for p, q in zip(path_p, path_q):
                if p == q:
                    res = p
                else:
                    break
            return res

        def dfs():
            # 三种情况root是p、q的最近公共祖先：
            #   1. p 和 q 在 root 的子树中，且分列 root 的 异侧
            #   2. p=root ，且 q 在 root 的左或右子树中
            #   3. q=root ，且 p 在 root 的左或右子树中
            def dfs(root, p, q):
                """root下如果没有p or q返回None, 如果有p or q就返回root"""
                if not root or root == p or root == q:
                    return root
                left = dfs(root.left, p, q)
                right = dfs(root.right, p, q)
                if not left:
                    return right
                if not right:
                    return left
                return root  # 1

            return dfs(root, p, q)

        return dfs()


# @lc code=end


func = Solution().lowestCommonAncestor
root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
p = 5
q = 1
print(func(root, p, q))
# 3

root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
p = 5
q = 4
print(func(root, p, q))
# 5

root = [1, 2]
p = 1
q = 2
print(func(root, p, q))
# 1
