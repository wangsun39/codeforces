# You are given two huge binary integer numbers a and b of lengths n and m respectively. You will repeat the following process: if b>0, then add to the answer the value a & b and divide b by 2 rounding down (i.e. remove the last digit of b), and repeat the process again, otherwise stop the process.
#
# The value a & b means bitwise AND of a and b. Your task is to calculate the answer modulo 998244353.
#
# Note that you should add the value a & b to the answer in decimal notation, not in binary. So your task is to calculate the answer in decimal notation. For example, if a=10102 (1010) and b=10002 (810), then the value a & b will be equal to 8, not to 1000.
#
# Input
# The first line of the input contains two integers n and m (1≤n,m≤2⋅105) — the length of a and the length of b correspondingly.
#
# The second line of the input contains one huge integer a. It is guaranteed that this number consists of exactly n zeroes and ones and the first digit is always 1.
#
# The third line of the input contains one huge integer b. It is guaranteed that this number consists of exactly m zeroes and ones and the first digit is always 1.
#
# Output
# Print the answer to this problem in decimal notation modulo 998244353.
#
# Examples
# inputCopy
# 4 4
# 1010
# 1101
# outputCopy
# 12
# inputCopy
# 4 5
# 1001
# 10101
# outputCopy
# 11
# Note
# The algorithm for the first example:
#
# add to the answer 10102 & 11012=10002=810 and set b:=110;
# add to the answer 10102 & 1102=102=210 and set b:=11;
# add to the answer 10102 & 112=102=210 and set b:=1;
# add to the answer 10102 & 12=02=010 and set b:=0.
# So the answer is 8+2+2+0=12.
#
# The algorithm for the second example:
#
# add to the answer 10012 & 101012=12=110 and set b:=1010;
# add to the answer 10012 & 10102=10002=810 and set b:=101;
# add to the answer 10012 & 1012=12=110 and set b:=10;
# add to the answer 10012 & 102=02=010 and set b:=1;
# add to the answer 10012 & 12=12=110 and set b:=0.
# So the answer is 1+8+1+0+1=11.

# https://codeforces.com/contest/1066/problem/E

MOD = 998244353

def func():  # 计算a中每个1对ans的贡献
    [n, m] = [int(i) for i in input().split(' ')]
    a = input()
    b = input()
    # n, m = 4, 4
    # a, b = '1010', '1101'
    # n, m = 4, 5
    # a, b = '1001', '10101'

    if len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    else:
        b = '0' * (len(a) - len(b)) + b
    N = max(n, m)
    oneNum = b.count('1')
    i, base, cnt = N - 1, 1, 0
    ans = 0
    while i >= 0:
        if a[i] == '1':
            ans += (base * (oneNum - cnt))
            ans %= MOD
        base *= 2
        base %= MOD
        if b[i] == '1':
            cnt += 1
        i -= 1

    print(ans)



if __name__ == '__main__':
    func()
