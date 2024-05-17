K, N = map(int,input().split())

ans = []

def choose(curr_num):

    if curr_num == N + 1:
        if N >= 3:
            for j in range(N-2):
                if ans[j] == ans[j+1] == ans[j+2]:
                    return
        print(*ans)
        return

    for i in range(1,K+1):
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()
choose(1)