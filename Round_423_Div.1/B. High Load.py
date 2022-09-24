# Arkady needs your help again! This time he decided to build his own high-speed Internet exchange point. It should consist of n nodes connected with minimum possible number of wires into one network (a wire directly connects two nodes). Exactly k of the nodes should be exit-nodes, that means that each of them should be connected to exactly one other node of the network, while all other nodes should be connected to at least two nodes in order to increase the system stability.
#
# Arkady wants to make the system as fast as possible, so he wants to minimize the maximum distance between two exit-nodes. The distance between two nodes is the number of wires a package needs to go through between those two nodes.
#
# Help Arkady to find such a way to build the network that the distance between the two most distant exit-nodes is as small as possible.
#
# Input
# The first line contains two integers n and k (3 ≤ n ≤ 2·105, 2 ≤ k ≤ n - 1) — the total number of nodes and the number of exit-nodes.
#
# Note that it is always possible to build at least one network with n nodes and k exit-nodes within the given constraints.
#
# Output
# In the first line print the minimum possible distance between the two most distant exit-nodes. In each of the next n - 1 lines print two integers: the ids of the nodes connected by a wire. The description of each wire should be printed exactly once. You can print wires and wires' ends in arbitrary order. The nodes should be numbered from 1 to n. Exit-nodes can have any ids.
#
# If there are multiple answers, print any of them.
#
# Examples
# inputCopy
# 3 2
# outputCopy
# 2
# 1 2
# 2 3
# inputCopy
# 5 3
# outputCopy
# 3
# 1 2
# 2 3
# 3 4
# 3 5
# Note
# In the first example the only network is shown on the left picture.
#
# In the second example one of optimal networks is shown on the right picture.
#
# Exit-nodes are highlighted.



# https://codeforces.com/contest/827/problem/B

# Tutorial: Since 1 ≤ ai ≤ 2, it's equivalent to find a longest subsequence like 1 * 2 * 1 * 2 * . By an easy dynamic programming we can find it in O(n) or O(n2) time. You can see O(n2) solution in the model solution below. Here we introduce an O(n) approach: Since the subsequence can be split into 4 parts (11...22...11...22...) , we can set dp[i][j](i = 1...n, j = 0..3) be the longest subsequence of a[1...i] with first j parts.
from functools import lru_cache


# def func(n, k):
# 本题 用递归会超过最大递归次数，化为迭代


def func():
    if n - k == 1:
        print(2)
        for i in range(2, n + 1):
            print('%d %d' % (1, i))
        return
    if n - k == 2:
        print(3)
        print('1 2')
        print('1 3')
        for i in range(4, n + 1):
            print('2 %d' % i)
        return
    if k * 2 >= n - 1:
        print(4)
        for i in range(2, n - k + 1):
            print('1 %d' % i)
            print('%d %d' % (i, i + n - k - 1))
        for i in range(n * 2 - k * 2, n + 1):
            print('1 %d' % i)
    else:
        if (n - 1) % k > 1:
            print((n - 1) // k * 2 + 2)
        elif (n - 1) % k == 1:
            print((n - 1) // k * 2 + 1)
        else:
            print((n - 1) // k * 2)
        s1, s2 = divmod(n - 1, k)
        for i in range(1, s1 + 1):
            if i == s1:
                for j in range(1, s2 + 1):
                    print((i - 1) * k + j, (i - 1) * k + j + k)
                break
            for j in range(1, k + 1):
                print((i - 1) * k + j, (i - 1) * k + j + k)
        for i in range(1, k + 1):
            print('%d %d' % (n, n - i))






if __name__ == '__main__':
    n, k = [int(i) for i in input().split(' ')]
    # n, k = 3, 2
    # n, k = 4, 2
    # n, k = 5, 3
    # n, k = 6, 3
    # n, k = 6, 2
    # n, k = 8, 3
    # n, k = 1000, 245
    func()


