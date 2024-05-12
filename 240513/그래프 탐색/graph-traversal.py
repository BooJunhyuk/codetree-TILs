# 그래프 G = (V, E)
# DFS : 재귀함수(stack) -> 보통 인접 리스트 사용
# BFs : Queue


N, M = map(int,input().split())

graph = [
    []
    for _ in range(N+1)
]
# 1부터 N까지의 인덱스를 사용하기 위해서 N+1

visited = [
    False
    for _ in range(N+1)
]

# def dfs(vertex):
#     for curr_v in graph[vertex]:
#         if not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)

def dfs(curr):
    global answer

    for nxt in graph[curr]:
        if visited[nxt]:
            continue
        answer += 1
        visited[nxt] = True
        dfs(nxt)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited[1] = True
dfs(1)

print(answer)