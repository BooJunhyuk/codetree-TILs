n = int(input())

visited = [
    False 
    for _ in range(n+1)
]

ans = []

def choose(curr_num):
    if curr_num == n + 1:
        print(*ans)
        return

    

    for i in range(1,n+1):
        if not visited[i]:
            ans.append(i)
            visited[curr_num] = True

            choose(curr_num + 1)
            
            ans.pop()
            visited[i] = False


choose(1)