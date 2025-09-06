x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
OFFSET = 1000
MAX_R = 2000

n = 3

checked = [
    [0]*(MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i in range(3):
    xa = x1[i] + OFFSET
    xa = x1[i] + OFFSET