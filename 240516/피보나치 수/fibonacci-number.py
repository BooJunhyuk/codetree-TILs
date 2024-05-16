# 1. DP 배열의 정의
#  DP[i] : i번째 피보나치 수

# 2. 점화식 세우기
# DP[i] = DP[i-1] + DP[i-2]

# 3. 구현


n = int(input())
dp = [1]*(n+1)


for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])