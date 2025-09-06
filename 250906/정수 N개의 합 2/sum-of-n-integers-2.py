n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

prefix_sum = [0] * (n + 1)


for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i-1]

max_sum = -10**9
for i in range(n-k+1):
    curr = prefix_sum[i+k] - prefix_sum[i]
    max_sum = max(max_sum, curr)

print(max_sum)