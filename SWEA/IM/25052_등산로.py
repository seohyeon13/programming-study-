T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            cur_x = i
            cur_y = j

            while 1:
                x = cur_x
                y = cur_y
                for i in range(4):
                    nx = x+ dx[i]
                    ny = y + dy[i]

                    if nx <0 or ny<0 or nx>=N or ny >= N:
                        continue

                    if arr[nx][ny] < arr[cur_x][cur_y]:
                        x = nx
                        y = ny

                if cur_x == x and cur_y == y:
                    break

                cur_x = x
                cur_y = y
                cnt += 1
            answer = max(cnt, answer)
    print(f'#{tc} {answer}')



                    
                    




            
