A = input()
B = input()

A_L = len(A)
B_L = len(B)

while B in A:
    for i in range(A_L-B_L+1):
        if A[i:i+B_L] == B:
            A = A[:i] + A[i+B_L:]
            A_L = len(A)
    
print(A)


# A = input().strip()
# B = input().strip()

# while B in A:
#     A = A.replace(B, "", 1)  # 첫 번째로 등장하는 B를 삭제

# print(A)
# '''
# 1. A와 B를 입력받습니다. strip()을 사용하여 입력 문자열의 양쪽 끝에 있는 공백을 제거합니다.
# 2. while B in A: 조건문을 사용하여 문자열 B가 A에 있는 동안 반복합니다.
# 3. A.replace(B, "", 1)을 사용하여 첫 번째로 등장하는 B를 빈 문자열로 대체하여 삭제합니다.
# 4. 최종적으로 남은 문자열 A를 출력합니다.
# '''