# You are given two arrays a and b of positive integers, with length n and m respectively.
#
# Let c be an n×m matrix, where ci,j=ai⋅bj.
#
# You need to find a subrectangle of the matrix c such that the sum of its elements is at most x, and its area (the total number of elements) is the largest possible.
#
# Formally, you need to find the largest number s such that it is possible to choose integers x1,x2,y1,y2 subject to 1≤x1≤x2≤n, 1≤y1≤y2≤m, (x2−x1+1)×(y2−y1+1)=s, and
# ∑i=x1x2∑j=y1y2ci,j≤x.
# Input
# The first line contains two integers n and m (1≤n,m≤2000).
#
# The second line contains n integers a1,a2,…,an (1≤ai≤2000).
#
# The third line contains m integers b1,b2,…,bm (1≤bi≤2000).
#
# The fourth line contains a single integer x (1≤x≤2⋅109).
#
# Output
# If it is possible to choose four integers x1,x2,y1,y2 such that 1≤x1≤x2≤n, 1≤y1≤y2≤m, and ∑x2i=x1∑y2j=y1ci,j≤x, output the largest value of (x2−x1+1)×(y2−y1+1) among all such quadruplets, otherwise output 0.
#
# Examples
# inputCopy
# 3 3
# 1 2 3
# 1 2 3
# 9
# outputCopy
# 4
# inputCopy
# 5 1
# 5 4 2 4 5
# 2
# 5
# outputCopy
# 1

# https://codeforces.com/contest/1060/problem/C

def subrect():
    [n, m] = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    x = int(input())
    # n, m = 3, 3  # 4
    # a = [1, 2, 3]
    # b = [1, 2, 3]
    # x = 9
    # n, m = 5, 1  # 4
    # a = [5, 4, 2, 4, 5]
    # b = [2]
    # x = 5
    def helper(l):
        n = len(l)
        res = [1e10] * n
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += l[j]
                res[j - i] = min(res[j - i], cur_sum)
        return res
    aa, bb = helper(a), helper(b)  # aa[i] 表示 a[i] 中长度为 i+1的子数组的最小和
    bb = bb[::-1]
    # print(aa, bb)
    i, j = 0, 0
    ans = 0
    # 以下用双指针
    while i < n and j < m:
        if aa[i] * bb[j] <= x:  # 边长为i+1,和边长为j+1的矩形内元素和为 aa[i] * bb[j]
            ans = max(ans, (i + 1) * (m - j))
            i += 1
        else:
            j += 1
    print(ans)


if __name__ == '__main__':
    subrect()
