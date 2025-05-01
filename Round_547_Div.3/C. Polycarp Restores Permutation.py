

# https://codeforces.com/problemset/problem/1141/C

from itertools import accumulate


def func(n, nums):
    s = list(accumulate(nums, initial=0))
    mn, mx = min(s), max(s)
    delta = n - mx
    ans = [str(x + delta) for x in s if x + delta > 0]
    if len(set(ans)) < n:
        print(-1)
        return
    # print(ans)
    print(' '.join(ans))
    return ans

if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    func(n, nums)

n = int(input())
nums = [int(x) for x in input().split(' ')]
s = list(accumulate(nums, initial=0))
mn, mx = min(s), max(s)

delta = n - mx
ans = [str(x + delta) for x in s if x + delta > 0]
if len(set(ans)) < n:
    print(-1)
else:
    print(' '.join(ans))



# input()
# s = 0
# l = [0]
# for i in map(int, input().split()):
#     s += i
#     l.append(s)
# m = 1 - min(l)
# l = tuple(map(lambda x: m + x, l))
# if len(l) == len(set(l)) == max(l) - min(l) + 1:
#     print(*l)
# else:
#     print(-1)