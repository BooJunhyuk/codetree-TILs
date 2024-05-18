A = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int,input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = input()


# 2024년 2월 5일이 월요일 + 7 월요일 + 

# 일수 계산
day_sum = 0
for i in range(m1,m2):
    day_sum += (days[m1] - d1 +1)

day_sum += d2

cnt = day_sum // 7
cnt1 = day_sum%7

if A[cnt1] == day:
    cnt+=1

print(cnt)