s, q = input().split()

# 1. s[1:] + s[0]
# 2. s[-1] + s[:-1]
# 3. s[: : -1]

q = int(q)
for i in range(q):
    a = int(input())

    if a == 1:
        s = s[1:] + s[0]
        print(s)

    elif a == 2:
        s = s[-1] + s[:-1]
        print(s)

    elif a == 3:
        s = s[::-1]
        print(s)