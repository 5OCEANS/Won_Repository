#17070 - 파이프 옮기기1
N = int(input())
walls = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for i in range(N)] for i in range(N)]for i in range(3)]

dp[0][0][1] = 1

for i in range(2,N):
    if walls[i] == 0:
        dp [0][0][i] = dp[0][0][i-1]

for r in range(1, N):
    for c in range(1, N):

        if walls[r][c] == 0 and walls[r][c - 1] == 0 and walls[r - 1][c] == 0:
            dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if walls[r][c] == 0:
            dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
            dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

print(sum(dp[i][N - 1][N - 1] for i in range(3)))
