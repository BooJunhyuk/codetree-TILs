# nCm = n개중 m개 뽑기

N, M = map(int,input().split())

# 1이상 N 이하 
# M 개 고르기

cnt = 0
ans = []

# 길이 N이고 1의 개수가 M인 것을 만들거에요.
# 0 혹은 1로 채울건데,
# 첫 번째부터 curr_num-1번째까지 이미 채운 상태에서...
# curr_num번째를 채울거고
# 지금 상태는 1의 개수가 one_cnt인 상황

def choose(curr_num,one_cnt):
    #종료 조건
    if curr_num == N + 1:
        if one_cnt == M:
            print(*ans)
            # for i in range(N):
            #     if ans[i] == 1:
            #         print(i+1, end=" ")
            # print()
        return

    
    #호출
    # ans.append(1)
    # choose(curr_num+1, one_cnt+1)
    # ans.pop()

    # ans.append(0)
    # choose(curr_num+1, one_cnt)
    # ans.pop()
    ans.append(curr_num)
    choose(curr_num+1, one_cnt+1)
    ans.pop()

    choose(curr_num+1, one_cnt)

    

choose(1,0)