
T = int(input())

dx = [-1, 1, 0, 0] # 상. 하. 좌. 우
dy = [0, 0, -1, 1]

for test_case in range(1, T+1):
    H, W = map(int, input().split())

    game_map = [list(input()) for _ in range(H)]

    N = int(input())

    command_list = list(input())

    dir = 0 # 방향 인덱스
    curr_x = 0
    curr_y = 0

    for i in range(H):
        for j in range(W):
            if game_map[i][j] == '^':
                dir = 0
                curr_x = i
                curr_y = j
            elif game_map[i][j] == 'v':
                dir = 1
                curr_x = i
                curr_y = j
            elif game_map[i][j] == '<':
                dir = 2
                curr_x = i
                curr_y = j
            elif game_map[i][j] == '>':
                dir = 3
                curr_x = i
                curr_y = j

    for command in command_list:
        if command == 'S':
            if dir == 0:
                for i in range(curr_x-1, -1, -1):
                    if game_map[i][curr_y] == '*':
                       game_map[i][curr_y] = '.'
                       break
                    elif game_map[i][curr_y] == '#':
                        break

            elif dir == 1:
                for i in range(curr_x+1, H):
                    if game_map[i][curr_y] == '*':
                       game_map[i][curr_y] = '.'
                       break
                    elif game_map[i][curr_y] == '#':
                        break

            elif dir == 2:
                for i in range(curr_y-1, -1, -1):
                    if game_map[curr_x][i] == '*':
                       game_map[curr_x][i] = '.'
                       break
                    elif game_map[curr_x][i] == '#':
                        break
            elif dir == 3:
                for i in range(curr_y+1, W):
                    if game_map[curr_x][i] == '*':
                       game_map[curr_x][i] = '.'
                       break
                    elif game_map[curr_x][i] == '#':
                        break
            

        elif command == 'U':
            dir = 0
            nx = curr_x+dx[dir]
            ny = curr_y+dy[dir]
            if 0<=nx<=(H-1) and 0<=ny<=(W-1) and game_map[nx][ny] == '.':
                game_map[curr_x][curr_y] = '.'
                curr_x = nx
                curr_y = ny
            game_map[curr_x][curr_y] = '^'

        elif command == 'D':
            dir = 1
            nx = curr_x+dx[dir]
            ny = curr_y+dy[dir]
            if 0<=nx<=(H-1) and 0<=ny<=(W-1) and game_map[nx][ny] == '.':
                game_map[curr_x][curr_y] = '.'
                curr_x = nx
                curr_y = ny
            game_map[curr_x][curr_y] = 'v'
      
        elif  command == 'L':
            dir = 2
            nx = curr_x+dx[dir]
            ny = curr_y+dy[dir]
            if 0<=nx<=(H-1) and 0<=ny<=(W-1) and game_map[nx][ny] == '.':
                game_map[curr_x][curr_y] = '.'
                curr_x = nx
                curr_y = ny
            game_map[curr_x][curr_y] = '<'
 
        elif command == 'R':
            dir = 3
            nx = curr_x+dx[dir]
            ny = curr_y+dy[dir]
            if 0<=nx<=(H-1) and 0<=ny<=(W-1) and game_map[nx][ny] == '.':
                game_map[curr_x][curr_y] = '.'
                curr_x = nx
                curr_y = ny
            game_map[curr_x][curr_y] = '>'

    print(f'#{test_case} ', end = '')
    for i in range(H):
        print(''.join(game_map[i]))

    