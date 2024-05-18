a = input()
b = input()

a = list(a)
b = list(b)

a_arr = []
b_arr = []
for i in range(len(a)):
    if '0'<= a[i] <='9':
        x = a[i]
        x = str(x)
        a_arr.append(x)
for i in range(len(b)):
    if '0'<= b[i] <='9':
        b_arr.append(b[i])


print(int(''.join(a_arr)) + int(''.join(b_arr)))