
from collections import Counter
from collections import defaultdict
from typing import List
from collections import deque
import copy
from functools import lru_cache


from collections import Counter
from functools import lru_cache

def treasure():
    # s = input()
    # s = '()((#((#(#()'  # 1 1 3
    s = '((#('   # -1
    # s = '(((#)((#)'
    # s = '()((#((#(#()'
    n = len(s)
    pos = []
    cur = 0
    left = []
    for i in range(n):
        if s[i] == '(':
            cur += 1
        elif s[i] == ')':
            cur -= 1
        else:
            cur -= 1
            pos.append(i)
        left.append(cur)
        if cur < 0:
            print(-1)
            return

    ans = [1] * len(pos)
    leftNum, rightNum = s.count('('), s.count(')')
    need = leftNum - rightNum
    ans[-1] = need - (len(pos) - 1)
    if ans[-1] > left[pos[-1]] + 1:
        print(-1)
        return
    for i in range(pos[-1] + 1, n):
        if left[i] < ans[-1] - 1:
            print(-1)
            return
    for e in ans:
        print(e)




if __name__ == '__main__':
    treasure()

# 3 3 3
# 2 2 2
# 1 1 3

# 4 7 9
# 5 2 7 3
# 3 5 2 7 3 8 7
