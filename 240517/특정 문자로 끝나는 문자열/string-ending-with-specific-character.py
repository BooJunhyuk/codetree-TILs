# 문자열을 구현하여 입력받습니다.
string = [
	input()
	for _ in range(10)
]

# 문자를 입력받습니다.
a = input()
cnt = 0

#print(string[1][-1])
# 마지막 문자로 주어진 문자가 나오는 경우 그 문자열을 출력합니다. 그리고 그런 횟수를 구합니다.
for i in range(10):
	leng = len(string[i])
	if string[i][leng-1] == a:
		print(string[i])
		cnt += 1
	
# 만족하는 문자열이 없다면 None을 출력합니다.
if cnt == 0:
	print("None")