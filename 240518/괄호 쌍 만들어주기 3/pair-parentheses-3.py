# # arr = input()


# # n = len(arr)
# # cnt = 0

# # for i in range(n):
# #     if arr[i] == "(":
# #         for j in range(i+1,n):
# #             if arr[j] == ")":
# #                 cnt += 1

# # print(cnt)


# # 변수 선언 및 입력
# string = input()
# n = len(string)
# print(string)
# print(string[1])
# # 모든 쌍을 다 잡아봅니다.
# cnt = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if string[i] == '(' and string[j] == ')':
#             cnt += 1
            
# print(cnt)


# S = input()
# answer = 0
# for i in range(len(S)):
#     for j in range(i+1, len(S)):
#         if S[i] == "(" and S[j] == ")":
#             answer +=1


# print(answer)

answer = 0
cnt = 0 # 지금까지 중 여는 괄호의 개수

for s in input():
    if s == "()":
        cnt += 1
    else:
        answer += cnt

print(answer)