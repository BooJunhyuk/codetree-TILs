#Choose(int curr_num)
#  - 첫 번째부터 curr_num - 1번째 까지는 모두 선택이 완료되었다.
#  - curr_num번째 위치에 0 혹은 1을 선택하는 함수














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