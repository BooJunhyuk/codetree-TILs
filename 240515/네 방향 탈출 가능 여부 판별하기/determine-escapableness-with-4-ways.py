from collections import deque

N, M = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(N)
]
# 뱀 있으면 1, 없으면 0

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

q = deque()

dxs = [0,1,-1,0]
dys = [1,0,0,-1]


def bfs():

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if 0<= nx < N and 0<= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))

visited[0][0] = True
q.append((0,0))

bfs()
# if visited[-1][-1]:
#     print(1)
# else:
#     print(0)
print(1 if visited[-1][-1] else 0)


#python 3항 연산자
# value1 if <statement> else value2
# if <statment>:
#       res = value1
#else:
#       res = value2