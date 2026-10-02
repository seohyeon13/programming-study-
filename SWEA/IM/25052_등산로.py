T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N):
            cur_x = i
            cur_y = j
            cnt = 1

            while 1:
                x = cur_x
                y = cur_y
                for i in range(4):
                    nx = cur_x+ dx[i]
                    ny = cur_y + dy[i]

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



                    
                    




            
