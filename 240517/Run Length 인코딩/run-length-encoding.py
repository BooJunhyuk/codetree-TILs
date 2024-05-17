# 변수 선언 및 입력:
A = input()

# 변환
encoded = ""

# 입력의 첫번째 값을 읽고 초기화합니다.
curr_char = A[0]
num_char = 1
for traget_char in A[1:]:
    if traget_char == curr_char:
        # 지금까지의 문자와 같으면 연속된 문자 개수만 추가해 주고 넘어갑니다.
        num_char += 1
    else:
        # 지금까지의 문자와 다르면 새로운 문자로 바꿔줘야 합니다.
        # 지금까지 세어온 curr_char와 num_char를 기록합니다.
        encoded += curr_char
        encoded += str(num_char)

        # curr_char와 num_char를 현재 값으로 초기화합니다.
        curr_char = traget_char
        num_char = 1
    
# 마지막 덩어리에 해당하는 curr_char와 num_char를 기록합니다.
encoded += curr_char
encoded += str(num_char)

print(len(encoded))
print(encoded)