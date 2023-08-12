# 有 N件物品和一个容量是 V的背包。每件物品只能使用一次。

# 第 i件物品的体积是 vi，价值是 wi。

# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。

# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

# 接下来有 N行，每行两个整数 vi,wi，用空格隔开，分别表示第 i件物品的体积和价值。

# 输出格式
# 输出一个整数，表示最大价值。

# 数据范围
# 0<N,V≤1000

# 0<vi,wi≤1000
# 输入样例
# 4 5
# 1 2
# 2 4
# 3 4
# 4 5
# 输出样例：
# 8
"""
N,V = list(map(int,input().split())) # 东西的件数，背包的容积
nums = [([0]*2) for i in range(N)]
for i in range(0,N,1):
    # print(input())
    nums[i][0],nums[i][1] =  list(map(int,input().split()))
    # print("---------")
    # print(nums)
f = [([0]*(V+1))for i in range(N+1)]
# print("---------")
# print(nums)
# print("---------")
for i in range(1,N+1,1):
    vi = nums[i-1][0]
    wi = nums[i-1][1]
    for j in range(0,V+1,1):
        # print(i,j)
        # print(f[i-1][j])
        f[i][j] = f[i-1][j] 
        if j>=vi:
            f[i][j] = max(f[i][j],f[i-1][j-vi]+wi)
    # print(f[i][:])
print(f[N][V])
"""
# 01背包变形，简化版本 只用一维数组进行存储
"""N,V = list(map(int,input().split())) # 东西的件数，背包的容积
nums = [([0]*2) for i in range(N)]
for i in range(0,N,1):
    # print(input())
    nums[i][0],nums[i][1] =  list(map(int,input().split()))
    # print("---------")
    # print(nums)
f = [0]*(V+1)
# print("---------")
# print(nums)
# print("---------")
for i in range(1,N+1,1):
    vi = nums[i-1][0]
    wi = nums[i-1][1]
    for j in range(V,0,-1):
        # print(i,j)
        # print(f[i-1][j])
        # f[j] = f[j-1] 
        if j>=vi:
            f[j] = max(f[j],f[j-vi]+wi)
    # print(f)
print(f[V])"""
# 完全背包问题，朴素写法会超时，因为有三重循环
"""N,V = list(map(int,input().split())) # 东西的件数，背包的容积
nums = [([0]*2) for i in range(N)]
for i in range(0,N,1):
    nums[i][0],nums[i][1] =  list(map(int,input().split()))
f = [([0]*(V+1))for i in range(N+1)]
for i in range(1,N+1,1):
    vi = nums[i-1][0]
    wi = nums[i-1][1]
    for j in range(0,V+1,1):
        # 超时写法
        f[i][j] = f[i-1][j]
        max_value = 0
        for k in range(1,j//vi+1,1): 
            tmp = f[i-1][j-k*vi]+k*wi
            if tmp>max_value:
                max_value = tmp
        f[i][j] = max(f[i][j],max_value)
print(f[N][V])
"""
# 完全背包问题，优化，不超时
"""N,V = list(map(int,input().split())) # 东西的件数，背包的容积
nums = [([0]*2) for i in range(N)]
for i in range(0,N,1):
    nums[i][0],nums[i][1] =  list(map(int,input().split()))
f = [([0]*(V+1))for i in range(N+1)]
for i in range(1,N+1,1):
    vi = nums[i-1][0]
    wi = nums[i-1][1]
    for j in range(0,V+1,1):
        f[i][j] = f[i-1][j] 
        if j>=vi:
            f[i][j] = max(f[i][j],f[i][j-vi]+wi)
print(f[N][V])"""

# 变形写法 只用一维度
N,V = list(map(int,input().split())) # 东西的件数，背包的容积
nums = [([0]*2) for i in range(N)]
for i in range(0,N,1):
    nums[i][0],nums[i][1] =  list(map(int,input().split()))
f = [0]*(V+1)
for i in range(1,N+1,1):
    vi = nums[i-1][0]
    wi = nums[i-1][1]
    for j in range(vi,V+1,1):
        f[j] = max(f[j],f[j-vi]+wi)
print(f[V])