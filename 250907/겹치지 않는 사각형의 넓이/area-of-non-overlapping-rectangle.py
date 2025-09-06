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

for i in range(3): # i = 0, 1, 2
    xa = x1[i] + OFFSET
    ya = y1[i] + OFFSET
    xb = x2[i] + OFFSET
    yb = y2[i] + OFFSET

    color = i + 1 # color 1, 2, 3
    for x in range(xa,xb):
        for y in range(ya, yb):
            checked[x][y] = color

area = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 1 or checked[x][y] == 2:
            area += 1
print(area)