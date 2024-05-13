# BFS 가 더 좋음 A -> B 로 갈 수 있는지?
# DFS 재귀호출 => 비용 증가

N, M = map(int, input().split())

A = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

dxs = [0,1]
dys = [1,0]

def dfs(x, y):
    visited[x][y] = True # dfs는 진입하고 적어주면 깔끔

    for dx, dy in zip(dxs, dys):# 0,1 /  1,0
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and A[nx][ny] == 1:
            dfs(nx, ny)

dfs(0, 0)
#python 3항 연산자
# value1 if <statement> else value2
# if <statment>:
#       res = value1
#else:
#       res = value2

# if visited[-1][-1]:
#     print(1)
# else:
#     print(0)

print(1 if visited[-1][-1]else 0)