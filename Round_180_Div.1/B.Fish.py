
from collections import Counter

def fish():
    [n, m, k] = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]

    if len(a) > len(b):
        print('YES')
        return
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i] > b[i]:
            print('YES')
            return
    print('NO')



if __name__ == '__main__':
    fish()

# 7 7 10
# 8 2 8 10 6 9 10
# 2 4 9 5 6 2 5

# 15 15 10
# 4 5 9 1 4 6 4 1 4 3 7 9 9 2 6
# 6 6 7 7 2 9 1 6 10 9 7 10 7 10 9
