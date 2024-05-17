s, q = input().split()

q = int(q)


arr = [
    list(input().split())
    for i in range(q)
]
s_arr = list(s)
#print(arr)

for i in range(q):
    
    if arr[i][0] == '1':
        a = int(arr[i][1])
        b = int(arr[i][2])

        s_arr[a-1], s_arr[b-1] = s_arr[b-1], s_arr[a-1]

        ans = ''.join(s_arr)
        print(ans)
        s_arr = list(ans)


    elif arr[i][0] == '2':
        x = arr[i][1]
        y = arr[i][2]
        for j in range(len(s)):
            if s_arr[j] == x:
                s_arr[j] = y

        ans = ''.join(s_arr)
        print(ans)
        s_arr = list(ans)