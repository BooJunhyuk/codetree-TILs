# 처음 0 
# 흰색 1 a
# 검은색 2 b



OFFSET = 2000

w = [0]*10000
b = [0]*10000
a = [0]*10000

n = int(input())

start = OFFSET

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        while x >0:
            a[start] = 2
            b[start] += 1
            x -= 1
            if x:
                start += 1


    elif d == 'L':
        while x >0:
            a[start] = 1
            w[start] += 1
            x -= 1

            if x:
                start -= 1

gray = 0
white = 0
black = 0
for i in range(10000):
    if w[i] >= 2 and b[i] >= 2:
        gray += 1
    elif  a[i] == 1:
        white += 1
    elif a[i] == 2:
        black += 1
print(white,black,gray)