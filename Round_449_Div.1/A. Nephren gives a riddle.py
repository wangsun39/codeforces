# Nephren is playing a game with little leprechauns.
#
# She gives them an infinite array of strings, f0... ∞.
#
# f0 is "What are you doing at the end of the world? Are you busy? Will you save us?".
#
# She wants to let more people know about it, so she defines fi =  "What are you doing while sending "fi - 1"? Are you busy? Will you send "fi - 1"?" for all i ≥ 1.
#
# For example, f1 is
#
# "What are you doing while sending "What are you doing at the end of the world? Are you busy? Will you save us?"? Are you busy? Will you send "What are you doing at the end of the world? Are you busy? Will you save us?"?". Note that the quotes in the very beginning and in the very end are for clarity and are not a part of f1.
#
# It can be seen that the characters in fi are letters, question marks, (possibly) quotation marks and spaces.
#
# Nephren will ask the little leprechauns q times. Each time she will let them find the k-th character of fn. The characters are indexed starting from 1. If fn consists of less than k characters, output '.' (without quotes).
#
# Can you answer her queries?
#
# Input
# The first line contains one integer q (1 ≤ q ≤ 10) — the number of Nephren's questions.
#
# Each of the next q lines describes Nephren's question and contains two integers n and k (0 ≤ n ≤ 105, 1 ≤ k ≤ 1018).
#
# Output
# One line containing q characters. The i-th character in it should be the answer for the i-th query.
#
# Examples
# inputCopy
# 3
# 1 1
# 1 2
# 1 111111111111
# outputCopy
# Wh.
# inputCopy
# 5
# 0 69
# 1 194
# 1 139
# 0 47
# 1 66
# outputCopy
# abdef
# inputCopy
# 10
# 4 1825
# 3 75
# 3 530
# 4 1829
# 4 1651
# 3 187
# 4 584
# 4 255
# 4 774
# 2 474
# outputCopy
# Areyoubusy
# Note
# For the first two examples, refer to f0 and f1 given in the legend.



# https://codeforces.com/contest/896/problem/A

# Tutorial: Since 1 ≤ ai ≤ 2, it's equivalent to find a longest subsequence like 1 * 2 * 1 * 2 * . By an easy dynamic programming we can find it in O(n) or O(n2) time. You can see O(n2) solution in the model solution below. Here we introduce an O(n) approach: Since the subsequence can be split into 4 parts (11...22...11...22...) , we can set dp[i][j](i = 1...n, j = 0..3) be the longest subsequence of a[1...i] with first j parts.
from functools import lru_cache


# def func(n, k):
# 本题 用递归会超过最大递归次数，化为迭代

@lru_cache(None)
def func(n, i):
    while True:
        if n == 0:
            if i < N1:
                return f0[i]
            else:
                return '.'
        l = lenf[n - 1] if n <= len(lenf) else lenf[-1]
        if i < N2:
            return f10[i]
        elif i < N2 + l:
            # return func(n - 1, i - 34)
            n -= 1
            i -= N2
        elif i < N2 + l + N3:
            return f11[i - (N2 + l)]
        elif i < N2 + l + N3 + l:
            n -= 1
            i -= (N2 + l + N3)
            # return func(n - 1, i - (34 + l + 32))
        elif i < N2 + l + N3 + l + N4:
            return f12[i - (N2 + l + N3 + l)]
        else:
            return '.'


if __name__ == '__main__':
    q = int(input())
    ans = ''
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
    f10 = "What are you doing while sending \""
    f11 = "\"? Are you busy? Will you send \""
    f12 = "\"?"
    N1, N2, N3, N4 = len(f0), len(f10), len(f11), len(f12)

    lenf = [N1]
    while lenf[-1] < 1e18:
        lenf.append(N2 + N3 + N4 + 2 * lenf[-1])
    # print(len(lenf))

    for i in range(q):
        n, k = [int(i) for i in input().split(' ')]
        # print(n, k)
        res = func(n, k - 1)
        ans += res
    print(ans)

