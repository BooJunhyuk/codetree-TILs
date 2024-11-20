from collections import deque

N = int(input())

r1, c1, r2, c2 = map(int,input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
# grid = [
#     list(map(int,input().split()))
#     for _ in range(N)
# ]

visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

step = [
    [0 for _ in range(N)]
    for _ in range(N)
]


q = deque()

dxs = [2,1,-1,-2,2,1,-1,-2]
dys = [1,2,2,1,-1,-2,-2,-1]


def bfs():

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                step[nx][ny] = step[x][y] + 1

visited[r1][c1] = True
q.append((r1,c1))
step[r1][c1] = 0
bfs()

#print(step[r2][c2])

print(step[r2][c2] if visited[r2][c2] else -1)

#print(1 if visited[-1][-1] else 0)



