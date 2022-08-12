# The new ITone 6 has been released recently and George got really keen to buy it. Unfortunately, he didn't have enough money, so George was going to work as a programmer. Now he faced the following problem at the work.
#
# Given a sequence of n integers p1, p2, ..., pn. You are to choose k pairs of integers:
#
# [l1, r1], [l2, r2], ..., [lk, rk] (1 ≤ l1 ≤ r1 < l2 ≤ r2 < ... < lk ≤ rk ≤ n; ri - li + 1 = m), 
# in such a way that the value of sum  is maximal possible. Help George to cope with the task.
#
# Input
# The first line contains three integers n, m and k (1 ≤ (m × k) ≤ n ≤ 5000). The second line contains n integers p1, p2, ..., pn (0 ≤ pi ≤ 109).
#
# Output
# Print an integer in a single line — the maximum possible value of sum.
#
# Examples
# inputCopy
# 5 2 1
# 1 2 3 4 5
# outputCopy
# 9
# inputCopy
# 7 1 3
# 2 10 7 18 5 33 0
# outputCopy
# 61

# https://codeforces.com/contest/467/problem/C

[n, m, k] = [int(i) for i in input().split(' ')]
p = [int(i) for i in input().split(' ')]

# [n, m, k] = [5,2,1]
# p = [1, 2, 3, 4, 5]  # 9

# [n, m, k] = [7, 1, 3]
# p = [2, 10, 7, 18, 5, 33, 0]  # 61
from functools import lru_cache

# [n, m, k] = [int(i) for i in '20 5 3'.split(' ')]  # 953
# p = [int(i) for i in '96 46 67 36 59 95 88 43 92 58 1 31 69 35 36 77 56 27 3 23'.split(' ')]

dp = [[0 for _ in range(n)] for _ in range(k)]
prefixS = []
s = 0

for j in range(n):
    s += p[j]
    prefixS.append(s)

# print(dp)
# print(prefixS)
# dp[i][j] 表示前j+1个字符，构造i+1个长度为m的子数组最大和

for i in range(0, k):
    for j in range(n):
        if j < m - 1:
            dp[i][j] = 0
        elif j == m - 1:
            dp[i][j] = prefixS[m - 1]
        else:
            if i > 0:
                dp[i][j] = max(dp[i - 1][j - m] + prefixS[j] - prefixS[j - m], dp[i][j - 1])
            else:
                dp[i][j] = max(prefixS[j] - prefixS[j - m], dp[i][j - 1])
print(dp[-1][-1])


