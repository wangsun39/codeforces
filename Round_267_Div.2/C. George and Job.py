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

# [n, m, k] = [int(i) for i in input().split(' ')]
# p = [int(i) for i in input().split(' ')]

# [n, m, k] = [5,2,1]
# p = [1, 2, 3, 4, 5]  # 9

# [n, m, k] = [7, 1, 3]
# p = [2, 10, 7, 18, 5, 33, 0]  # 61
from functools import lru_cache

[n, m, k] = [int(i) for i in '20 5 3'.split(' ')]
p = [int(i) for i in '96 46 67 36 59 95 88 43 92 58 1 31 69 35 36 77 56 27 3 23'.split(' ')]

@lru_cache(None)
def helper(idx, num):  # 从p[idx] 开始找 num 个子数组和的最大值
    if idx + m * k - 1 >= n:
        return False, -1
    ans = 0
    for i in range(idx, n - m + 1):
        if num > 1:
            res = helper(i + m, num - 1)
            if not res[0]:
                ans = max(ans, sum(p[i: i + m]))
                return True, ans
            ans = max(ans, sum(p[i: i + m]) + res[1])
        else:
            ans = max(ans, sum(p[i: i + m]))
    return True, ans


res = helper(0, k)
print(res[1])
