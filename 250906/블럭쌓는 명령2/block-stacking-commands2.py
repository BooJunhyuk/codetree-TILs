n, k = map(int, input().split())
commands = [
    tuple(map(int, input().split())) 
    for _ in range(k)
    ]

# Please write your code here.


blocks = [0]*(n)

for a, b in commands:
    for i in range(a-1, b):
        blocks[i] += 1


max_num = max(blocks)
print(max_num)
