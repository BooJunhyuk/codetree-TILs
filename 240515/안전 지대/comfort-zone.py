N, M = map(int,input().split())

graph = [
    list(map(int,input().split()))
    for _ in range(N)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def dfs(x, y):

    visited[x][y] = True

    for dx, dy in zip(dxs,dys):
        nx, ny = x +dx, y + dy
        if 0<= nx < N and 0<= ny < M and not visited[nx][ny]:
            dfs(nx, ny)

safe_area_cnt = 0 # 안전영역의 수
safe_area_cnt_arr = []
K = 0
for i in graph:
    for m in i:
        K = max(K,m)

for k in range(1, K+1):
    safe_area_cnt = 0
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]


    for i in range(N):
        for j in range(M):
            if graph[i][j] <= k:
                visited[i][j] = True
    for u in range(N):
        for v in range(M):
            if not visited[u][v]:
                dfs(u, v)
                safe_area_cnt += 1
    safe_area_cnt_arr.append(safe_area_cnt)

#print(safe_area_cnt_arr)
max_safe_area = 0
max_safe_area = max(safe_area_cnt_arr)

max_idx = safe_area_cnt_arr.index(max_safe_area)
print(max_idx+1,end=" ")
print(max_safe_area)