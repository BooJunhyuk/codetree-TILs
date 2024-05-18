# 변수 선언 및 입력:
n = int(input())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 시작 위치와 방향, 
# 해당 방향으로 이동할 횟수를 설정합니다.
curr_x, curr_y = n // 2, n // 2
move_dir, move_num = 0, 1

# 문제에서 원하는 진행 순서대로 
# 오른쪽 위 왼쪽 아래 방향이 되도록 정의합니다.
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

# 시작 위치와 방향, 
# 해당 방향으로 이동할 횟수를 설정합니다. 
cnt = 1

while True:
    # move_num 만큼 이동합니다.
    for _ in range(move_num):
        if 0 <= curr_x < n and 0 <= curr_y < n:
            grid[curr_x][curr_y] = cnt
            cnt += 1
        
        curr_x += dxs[move_dir]
        curr_y += dys[move_dir]
        
        # 이동하는 도중 격자를 벗어나게 되면,
        # 움직이는 것을 종료합니다.
        if not (0 <= curr_x < n and 0 <= curr_y < n):
            break
    
    if not (0 <= curr_x < n and 0 <= curr_y < n):
        break
    
    # 방향을 바꿉니다.
    move_dir = (move_dir + 1) % 4
    # 만약 현재 방향이 왼쪽 혹은 오른쪽이 된 경우에는
    # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
    if move_dir == 0 or move_dir == 2:
        move_num += 1

# 출력:
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()