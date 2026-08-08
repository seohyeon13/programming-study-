for _ in range(10):
    test_case = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    dx = [1, 0, 0] #하, 좌, 우
    dy = [0, -1, 1]
    result = 0

    for i in range(len(arr[0])):
        if arr[0][i]:
            cur_x = 0 # 시작 행
            cur_y = i # 시작 열

            d = 0 # 방향 (하, 좌, 우)

            while cur_x < 99:
                if d == 0: # 아래 방향
                    if cur_y-1>0 and arr[cur_x][cur_y-1] == 1:
                        d = 1

                    elif cur_y+1<99 and arr[cur_x][cur_y+1] == 1:
                        d = 2
                else:
                    if arr[cur_x+1][cur_y] == 1:
                        d = 0

                cur_x += dx[d]
                cur_y += dy[d]

            if arr[cur_x][cur_y] == 2:
                result = i
                break

    print(f'#{test_case} {result}')










                


        
