K,N = map(int,input().split())

ans = []

# 첫 번째부터 curr_num - 1 까지 선택을 했고, curr_num번째 수를 이제 고를 차례
def choose(curr_num):
    #종료조건
    if curr_num == N+1:
        print(*ans)
        #print(*ans,sep=" ")
        return
    #다음 내용 호출    
    for i in range(1,K+1):
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()

choose(1)