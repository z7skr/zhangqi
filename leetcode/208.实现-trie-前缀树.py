# @lc app=leetcode.cn id=208 lang=python3
# [208] 实现 Trie (前缀树)
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
# Medium (72.00%)
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
# Trie（发音类似 "try"）或者说 前缀树
# 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false
# 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
# ；否则，返回 false 。
# 示例：
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
# 提示：
# 1
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次


# @lc code=start
class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = dict()  # 初始化子节点
        self.isEnd = False  # isEnd 用于标记单词结束


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        def insert_t(word):
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
            cur.isEnd = True

        def insert_r(word, i=0, cur=self.root):
            if i == len(word):
                cur.isEnd = True
                return
            ch = word[i]
            if ch not in cur.children:
                cur.children[ch] = Node()
            insert_r(word, i + 1, cur.children[ch])

        insert_r(word)

    # 查找字典树中是否存在一个单词
    def search(self, word: str) -> bool:
        def search_t(word):
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]
            return cur.isEnd

        def search_r(word, i=0, cur=self.root):
            if i == len(word):
                return cur.isEnd
            ch = word[i]
            if ch not in cur.children:
                return False
            else:
                return search_r(word, i + 1, cur.children[ch])

        return search_t(word)

    # 查找字典树中是否存在一个前缀
    def startsWith(self, prefix: str) -> bool:
        def startsWith_t(prefix):
            cur = self.root
            for ch in prefix:
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]
            return True

        def startsWith_r(prefix, i=0, cur=self.root):
            if i == len(prefix):
                return True
            ch = prefix[i]
            if ch not in cur.children:
                return False
            else:
                return startsWith_r(prefix, i + 1, cur.children[ch])

        return startsWith_r(prefix)


# Your Trie object will be instantiated and called as such:

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
# @lc code=end
