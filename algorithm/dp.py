# 背包问题
def func_零一背包(N, V, v, w):
    """
    每种物品只有一个
    dp[i][j] = 前i个物品装进容量j的背包的最大价值
    参数:
    N (int): 物品的数量
    V (int): 背包的容量
    v (list): 每个物品的体积列表
    w (list): 每个物品的价值列表
    """
    def func_原始():
        dp = [[0] * (V + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, V + 1):
                if j < v[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v[i - 1]] + w[i - 1])
                # dp[i][j] = dp[i - 1][j]
                # if j >= v[i - 1]:
                #     dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i - 1]] + w[i - 1])
        print(dp[N][V])

    def func_空间优化():
        dp = [0] * (V + 1)
        for i in range(1, N + 1):
            # 因为要和前一行的j-v比较, 所以如果先更新了j-v就无法得出正确答案
            for j in range(V, v[i - 1] - 1, -1):  ## j >= v[i-1]
                dp[j] = max(dp[j], dp[j - v[i - 1]] + w[i - 1])
        print(dp[V])

    # func_原始()
    func_空间优化()

def func_完全背包(N, V, v, w):
    """
    每种物品无限个
    参数:
    N (int): 物品的数量
    V (int): 背包的容量
    v (list): 每个物品的体积列表
    w (list): 每个物品的价值列表
    """
    def func_原始():  # TLE
        dp = [[0] * (V + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, V + 1):
                # # 所有可能的i-1的数量都要试一下
                # t = j // v[i - 1]
                # for k in range(t + 1):
                #     dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v[i - 1]] + k * w[i - 1])
                # 只和前一个比较
                dp[i][j] = dp[i - 1][j]
                if j >= v[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j - v[i - 1]] + w[i - 1])
        print(dp[N][V])

    def func_空间优化():
        dp = [0] * (V + 1)
        for i in range(1, N + 1):
            for j in range(v[i - 1], V + 1):
                dp[j] = max(dp[j], dp[j - v[i - 1]] + w[i - 1])
        print(dp[V])
    
    # func_原始()
    func_空间优化()

def func_多重背包(N, V, v, w, s):
    """
    每种物品个数不一样，介于 01背包和完全背包之间
    参数:
    N (int): 物品种类数
    V (int): 背包容量
    v (list): 每种物品的体积列表
    w (list): 每种物品的价值列表
    s (list): 每种物品的数量列表
    思路:
    1. 将多重背包问题转化为01背包问题
    2. 使用二进制分解的方法将每种物品分解为若干个01背包问题
    3. 调用01背包问题的解决方案求解
    """
    nN, nv, nw = 0, [], []
    for i in range(N):
        k, c = 1, s[i]
        while c > 0:
            n = min(k, c)
            c -= n
            k <<= 1
            nN += 1
            nv.append(n * v[i])
            nw.append(n * w[i])
    # 01背包
    func_零一背包(nN, V, nv, nw)

def func_混合背包(N, V, v, w, s):
    """
    和多重背包不一样的是可以无限个
    参数:
    N (int): 物品种类数
    V (int): 背包容量
    v (list): 每种物品的体积列表
    w (list): 每种物品的价值列表
    s (list): 每种物品的数量列表，0表示无限，-1表示1次
    思路:
    1. 将每种物品根据数量进行处理，-1表示只能选一次，0表示可以选无限次
    2. 将处理后的物品转化为01背包问题
    3. 调用01背包问题的解决方案求解
    """
    nN, nv, nw = 0, [], []
    for i in range(N):
        k, c = 1, s[i]
        if c == -1:  # 只能选一次
            c = 1
        elif c == 0:  # 可以选无限次
            c = V // v[i]
        while c > 0:
            n = min(k, c)
            c -= n
            k, nN = k << 1, nN + 1
            nv.append(n * v[i])
            nv.append(n * v[i])
            nw.append(n * w[i])
    # 01背包
    func_零一背包(nN, V, nv, nw)

def func_分组背包(N, V, v, w, s):
    """
    参数:
    N: int - 物品种类数
    V: int - 背包容量
    v: List[List[int]] - 每种物品的体积列表
    w: List[List[int]] - 每种物品的价值列表
    s: List[int] - 每种物品的数量列表
    """
    def func_原始():
        dp = [[0] * (V + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, V + 1):
                dp[i][j] = dp[i - 1][j]
                for k in range(s[i - 1]):
                    if j >= v[i - 1][k]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i - 1][k]] + w[i - 1][k])
        print(dp[N][V])

    def func_空间优化():
        dp = [0] * (V + 1)
        for i in range(1, N + 1):
            for j in range(V, 0, -1):
                for k in range(s[i - 1]):
                    if j >= v[i - 1][k]:
                        dp[j] = max(dp[j], dp[j - v[i - 1][k]] + w[i - 1][k])
        print(dp[V])

    # func_原始()
    func_空间优化()

