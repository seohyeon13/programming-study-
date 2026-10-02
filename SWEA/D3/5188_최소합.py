T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0] # 하, 우
    dy = [0, 1]

    curr_x = 0
    curr_y = 0
    min = float('inf')
    sum = 0

    for x in range(N):
        if arr[curr_x + dx[0]][curr_y+dy[0]] >= arr[curr_x + dx[1]][curr_y+dy[1]]:
                sum += arr[curr_x+dx[1]][curr_y+dy[1]]
                curr_x += dx[1]
                curr_y += dy[1]
        if min > sum:
             min = sum
        


    print(f'#{test_case} {min}') 




