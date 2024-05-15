N = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(N)
]


visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

cnt = 0
bomb = 0
bomb_cnt = 0
bomb_arr = []

def dfs(x,y):
    global bomb, bomb_cnt, cnt
    visited[x][y] = True
    

    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy

        if 0<= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            dfs(nx,ny)
            bomb += 1
            print(bomb)
    #bomb_arr.append(bomb)
    if bomb >=4:
        bomb_cnt+=1
    cnt += 1

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bomb = 0
            dfs(i, j)
            bomb_arr.append(cnt)

#print(bomb_arr)

#print(bomb_cnt,max(bomb_arr))