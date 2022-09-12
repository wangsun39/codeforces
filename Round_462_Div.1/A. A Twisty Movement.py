# A. A Twisty Movement
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# A dragon symbolizes wisdom, power and wealth. On Lunar New Year's Day, people model a dragon with bamboo strips and clothes, raise them with rods, and hold the rods high and low to resemble a flying dragon.
#
# A performer holding the rod low is represented by a 1, while one holding it high is represented by a 2. Thus, the line of performers can be represented by a sequence a1, a2, ..., an.
#
# Little Tommy is among them. He would like to choose an interval [l, r] (1 ≤ l ≤ r ≤ n), then reverse al, al + 1, ..., ar so that the length of the longest non-decreasing subsequence of the new sequence is maximum.
#
# A non-decreasing subsequence is a sequence of indices p1, p2, ..., pk, such that p1 < p2 < ... < pk and ap1 ≤ ap2 ≤ ... ≤ apk. The length of the subsequence is k.
#
# Input
# The first line contains an integer n (1 ≤ n ≤ 2000), denoting the length of the original sequence.
#
# The second line contains n space-separated integers, describing the original sequence a1, a2, ..., an (1 ≤ ai ≤ 2, i = 1, 2, ..., n).
#
# Output
# Print a single integer, which means the maximum possible length of the longest non-decreasing subsequence of the new sequence.
#
# Examples
# inputCopy
# 4
# 1 2 1 2
# outputCopy
# 4
# inputCopy
# 10
# 1 1 2 2 2 1 1 2 2 1
# outputCopy
# 9
# Note
# In the first example, after reversing [2, 3], the array will become [1, 1, 2, 2], where the length of the longest non-decreasing subsequence is 4.
#
# In the second example, after reversing [3, 7], the array will become [1, 1, 1, 1, 2, 2, 2, 2, 2, 1], where the length of the longest non-decreasing subsequence is 9.

# https://codeforces.com/contest/933/problem/A

# Tutorial: Since 1 ≤ ai ≤ 2, it's equivalent to find a longest subsequence like 1 * 2 * 1 * 2 * . By an easy dynamic programming we can find it in O(n) or O(n2) time. You can see O(n2) solution in the model solution below. Here we introduce an O(n) approach: Since the subsequence can be split into 4 parts (11...22...11...22...) , we can set dp[i][j](i = 1...n, j = 0..3) be the longest subsequence of a[1...i] with first j parts.

def func1():

    dp = [[0] * 2 for _ in range(n)]
    ans = 0

    for i in range(n):
        x, y = 1, 0  # 对于a[i] == 1, x, y 分别表示以a[i]结尾的最长全1子序长度和 形如11122211 的最长子序
                     # 对于a[i] == 2, x, y 分别表示以a[i]结尾的最长全2子序长度和 形如1112221122 的最长子序
        if a[i] == 1:
            for j in range(i):
                if a[j] == 1:
                    x = max(dp[j][0] + 1, x)
                    y = max(dp[j][1] + 1, y)
                else:
                    y = max(dp[j][0] + 1, y)
        else:
            for j in range(i):
                x = max(dp[j][0] + 1, x)
                y = max(dp[j][1] + 1, y)
        dp[i][0], dp[i][1] = x, y
        ans = max(ans, dp[i][0], dp[i][1])
    # print(dp)
    print(ans)


def func():

    dp = [0] * 4
    # ans = 0

    for i in range(n):
        if a[i] == 1:
            dp[0] = dp[0] + 1
            dp[2] = max(dp[1], dp[2]) + 1
        else:
            dp[1] = max(dp[0], dp[1]) + 1
            dp[3] = max(dp[2], dp[3]) + 1
    print(max(dp))



if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split(' ')]

    # n = 4
    # a = [int(i) for i in '1 2 1 2'.split(' ')]
    # n = 10
    # a = [int(i) for i in '1 1 2 2 2 1 1 2 2 1'.split(' ')]

    func()

