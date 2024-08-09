# @lc app=leetcode.cn id=93 lang=python3
# [93] 复原 IP 地址
# https://leetcode.cn/problems/restore-ip-addresses/description/
# Medium (59.36%)
# Testcase Example:  '"25525511135"'
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能
# 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2：
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 提示：
# 1 <= s.length <= 20
# s 仅由数字组成


# @lc code=start
class Solution:
    from typing import List

    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(n, i, ip):
            """
            n: 还剩几个数字
            i: 当前s的序号
            ip: path
            """
            if n == 0 and i == len(s):
                res.append(".".join(ip))
            if n == 0 or i == len(s):
                return
            if s[i] == "0":
                ip.append("0")
                dfs(n - 1, i + 1, ip)
                ip.pop()
            else:
                j = i + 1
                while j <= len(s) and int(s[i:j]) < 256:
                    ip.append(s[i:j])
                    dfs(n - 1, j, ip)
                    ip.pop()
                    j += 1

        res, ip = [], []
        dfs(4, 0, ip)
        return res


# @lc code=end


func = Solution().restoreIpAddresses
s = "25525511135"
print(func(s))
# ["255.255.11.135","255.255.111.35"]

s = "0000"
print(func(s))
# ["0.0.0.0"]

s = "101023"
print(func(s))
# ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
