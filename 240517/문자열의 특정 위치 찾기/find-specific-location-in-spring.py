# s = 'appleabanana'
# print(s.find('bob'))

# s = 'appleabanana'

# if 'a' in s:
#     print(s.index('a'))
# else:
#     print(-1)

# 문자열과 문자를 입력받습니다.
string, a = tuple(input().split())
start_idx = -1

# 문자열의 길이를 구합니다.
length = len(string)

# 문자열 a가 존재하는지 확인하고 존재할 경우 그 인덱스를 기록합니다.
for i in range(length):
    if string[i] == a:
        start_idx = i
        break
        
# 문자열 a가 존재하지 않는다면 No를 출력합니다.
if start_idx == -1:
    print("No")
else:
    print(start_idx)