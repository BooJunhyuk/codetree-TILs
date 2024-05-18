# A = input()
# B = input()

# A_L = len(A)
# B_L = len(B)

# for i in range(A_L-B_L+1):
#     if A[i:i+B_L] == B:
#         A = A[:i] + A[i+B_L:]
#         A_L = A_L - B_L
#     else:


# print(A)


A = input().strip()
B = input().strip()

while B in A:
    A = A.replace(B, "", 1)  # 첫 번째로 등장하는 B를 삭제

print(A)