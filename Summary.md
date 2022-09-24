| 时间 | 题号 | 题目      | 难度 | 说明 |
|----|---------|-----|-----|--------|
|2022-9-24| Codeforces Round #423 (Div. 1)  B  | [High Load](https://codeforces.com/contest/827/problem/B) |    1800   | 一道图论的题，相对其他题容易一点，需要考虑充分各种场景 |
|2022-9-17| Codeforces Round #449 (Div. 1)  A  | [Nephren gives a riddle](https://codeforces.com/contest/896/problem/A) |    1700   | 想了好几天，开始打算用递归，后来发现递归会超过最大递归深度，或者栈空间不足的情况，实际只需要稍微改造一下，变成迭代的方式就可以。题目还是不错的，第一次遇到递归栈空间不够的情况 |
|2022-9-11| Codeforces Round #462 (Div. 1)  A  | [A Twisty Movement](https://codeforces.com/contest/933/problem/A) |    1800   | 想了两周，没想出来，开始看题解也没明白（开始题目都理解错了）<br>明白之后发现就是一个DP，关键还是把题目等价转换想出来，最长单调增子序，可以考虑DP或线段树<br>题目本质是将数组划分成 4 部分：11...22...11...22...，那么定义 dp[i][j] 表示前 i 个元素组成前 j 个部分的最长子序列的长度。 |
