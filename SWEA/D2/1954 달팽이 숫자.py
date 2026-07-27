T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    # print(arr)

    x = 0
    y = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0

    for num in range(1, N*N+1):
        arr[x][y] = num

        nx = x +dx[direction]
        ny = y +dy[direction]

        if (nx<N and ny<N) and (nx>=0 and ny >= 0) and arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            direction = (direction + 1)%4
            nx = x+dx[direction]
            ny = y+dy[direction]

            if (nx<N and ny<N) and (nx>=0 and ny >= 0):
                x = nx
                y = ny            


    print(f'#{test_case}')

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()
