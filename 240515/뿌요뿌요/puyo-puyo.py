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

block_size = 0
block_size_bomb = 0
block_size_arr = []
def dfs(x,y):
    global block_size
    visited[x][y] = True
    block_size += 1

    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy

        if 0<= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            block_size = 0
            dfs(i, j)
            if block_size >= 4: #블록사이즈가 4보다 크면 
                block_size_bomb += 1 # 1씩 증가 (터지는 개수)
            #그리고 블록사이즈 저장
            block_size_arr.append(block_size)

print(block_size_bomb, max(block_size_arr)) # 터지는 개수랑 블록 사이즈 최대 크기