
# KMP 匹配算法，T 为文本串，p 为模式串
def kmp(T: str, p: str) -> int:
    # next[j] 表示 模式串 p[0,j](包括j) 中，最长相等前后缀的长度
    # 以0开头的前缀串 == 以j结尾的后缀串，的最长长度
    # 如果T(i)和p[j]匹配不成功
    # aabaacbaab
    # 0101200123
    def generateNext(p: str):
        next = [0] * len(p)
        j = 0  # j 为前缀串的起始下标位置
        for i in range(1, len(p)):  # i 为后缀串的起始下标位置
            while j > 0 and p[i] != p[j]:  # 匹配不成功, j 回退
                j = next[j - 1]  # j 进行回退操作
            if p[i] == p[j]:  # 匹配成功，继续匹配，此时 j 为前缀长度
                j += 1
            next[i] = j  # 记录前缀长度，更新 next[i], 结束本次循环, i += 1
        return next

    next = generateNext(p)
    print(*next, sep="")
    j = 0  # j 为模式串中当前匹配的位置
    for i in range(len(T)):  # i 为文本串中当前匹配的位置
        while j > 0 and T[i] != p[j]:  # 匹配不成功, 将模式串回退
            j = next[j - 1]
        if T[i] == p[j]:  # 匹配成功，继续匹配
            j += 1
        if j == len(p):  # 当前模式串完全匹配成功，返回匹配开始位置
            return i - j + 1
    return -1  # 匹配失败，返回 -1

def test_kmp():
    print(kmp("aabcbdededffggffgghihi", "aabaacbaab"))
    print(kmp("mississippi", "ississi"))
    print(kmp("abbcfdddbddcaddebc", "bcf"))
    print(kmp("aaaaa", "bba"))
    print(kmp("ababbbbaaabbbaaa", "bbbb"))

# test_kmp()


# 字典树
class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = dict()  # 初始化子节点
        self.isEnd = False  # isEnd 用于标记单词结束

class Trie:  # 字典树
    def __init__(self):
        self.root = Node()

    # 向字典树中插入一个单词
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

        return insert_t(word)

    # 查找字典树中是否存在一个单词
    def search(self, word: str) -> bool:
        def search_t(word):
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]
            return cur is not None and cur.isEnd

        def search_r(word, i=0, cur=self.root):
            if i == len(word):
                return cur is not None and cur.isEnd
            ch = word[i]
            if ch not in cur.children:
                return False
            else:
                return search_r(word, i + 1, cur.children[ch])

        return search_r(word)

    # 查找字典树中是否存在一个前缀
    def startsWith(self, prefix: str) -> bool:
        def startsWith_t(prefix):
            cur = self.root
            for ch in prefix:
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]
            return cur is not None

        def startsWith_r(prefix, i=0, cur=self.root):
            if i == len(prefix):
                return cur is not None
            ch = prefix[i]
            if ch not in cur.children:
                return False
            else:
                return startsWith_r(prefix, i + 1, cur.children[ch])

        return startsWith_r(prefix)

def test_trie_operations():
    words = ["a", "app", "apple", "application", "apply", "banana"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.search("app"))

# test_trie_operations()
