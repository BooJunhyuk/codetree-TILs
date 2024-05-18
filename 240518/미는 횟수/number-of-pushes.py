a = input()
b = input()

cnt = 0

while True:

    cnt += 1
    a = a[-1] + a[:-1]
    if a == b:
        print(cnt)
        break