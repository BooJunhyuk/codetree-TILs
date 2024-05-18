a = input()
b = input()

cnt = 0

for i in range(len(a)-1):
    cnt += 1
    a = a[-1] + a[:-1]
    if a == b:
        print(cnt)
        break