n, t = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 1
max_val = 0


for i in range(1, len(arr)):

    if i > 1:
        if arr[i] > t and arr[i-1] > t:
            cnt += 1
            max_val = max(cnt, max_val)
        else:
            cnt = 1
    else:
        cnt = 1
        max_val = max(cnt, max_val)
print(max_val)