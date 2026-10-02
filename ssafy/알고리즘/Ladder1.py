for _ in range(1, 11):
    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    curr_x , curr_y = 0,0
    for col in range(100):
        if ladder[99][col] == 2:
            curr_x = 99
            curr_y = col
            break

    while curr_x >0:

        # 좌
        if curr_y > 0 and ladder[curr_x][curr_y-1] == 1:
            while curr_y > 0 and ladder[curr_x][curr_y-1] == 1:
                curr_y -= 1

        #  우
        elif curr_y < 99 and ladder[curr_x][curr_y+1] == 1:
            while curr_y < 99 and ladder[curr_x][curr_y+1] == 1:
                curr_y+=1

        curr_x -= 1

    print(f'#{tc} {curr_y}')