A = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' ]

m1, d1, m2, d2 = map(int,input().split())

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = input()


# 2024년 2월 5일이 월요일 + 7 월요일 + 

# 일수 계산
day_sum = 0
for i in range(m1,m2):
    if i == m1:
        day_sum += (days[m1] - d1 +1)
    else:
        day_sum +=days[i]

day_sum += d2

cnt = 0
for i in range(1, day_sum +1):
    if A[(1+i)%7] == day:
        cnt += 1
print(cnt)