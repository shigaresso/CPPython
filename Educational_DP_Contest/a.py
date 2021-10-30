import sys

def main():
    N, h, dp = initialize()
    solve(N, h, dp)

# 1行の読み込み
def input():
    return sys.stdin.readline().rstrip()

# 問題文の設定を読み込む
def initialize():
    N = int(input())
    h = [int(i) for i in input().split()]
    dp = [10**9] * N
    dp[0] = 0
    return N,h,dp

# 問題の解法
def solve(N, h, dp):
    for i in range(N):
        if i < N-1:
            dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
        if i < N-2:
            dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
    # 最後尾を表したい場合 N-1 と書かなくても良い
    print(dp[-1])

if __name__ == '__main__':
    main()