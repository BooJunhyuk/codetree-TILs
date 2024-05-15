N = int(input())

graph = [
    list(map(int,input().split()))
    for _ in range(N)
]# 사람이 있는 경우 1 , 벽이 있는 경우 0

visited = [
    [False for _ in range(N)]
    for _ in range(N)
] # 방문한 적이 있는지 체크
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

people = 0 # 사람 수
t = 0 # 마을 수
people_arr = []
def dfs(x, y):
    global people
    visited[x][y] = True

    for dx, dy in zip(dxs,dys):
        nx, ny = x +dx, y + dy
        if 0<= nx < N and 0<= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            people += 1
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            people = 1
            dfs(i,j)
            people_arr.append(people)
            t += 1


print(t)
#print(sorted(people_arr))
people_arr.sort()
for i in range(t):
    print(people_arr[i])
# for elem in people_arr:
#     print(*elem)
#print(*people_arr, end= '\n')
# for elem in visited:
#     for x in elem:
#         if x == False:
#             dfs(elem,x)