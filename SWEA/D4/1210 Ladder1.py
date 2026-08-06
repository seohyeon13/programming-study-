def route(x, y):

    dx = [1, 0, 0]    # 하 우 좌
    dy = [0, 1, -1]

    flag = True

    curr_x = x
    curr_y = y

    visited = [[0]*100 for _ in range(100)]

    while flag:

        # 도착
        if arr[curr_x][curr_y] == 2:
            return True

        visited[curr_x][curr_y] = 1

        # 아래 길 있으면
        if curr_x+1 >= 0 and curr_x+1 <100 and arr[curr_x+1][curr_y] in (1,2) and visited[curr_x+1][curr_y]==0: 
            curr_x += 1

        # 오른쪽 길 있으면
        elif curr_y+1 >= 0 and curr_y+1 <100 and arr[curr_x][curr_y+1] in (1,2) and visited[curr_x][curr_y+1]==0: 
            curr_y += 1

        # 왼쪽 길 있으면
        elif curr_y-1 >= 0 and curr_y-1<100 and arr[curr_x][curr_y-1] in (1,2) and visited[curr_x][curr_y-1]==0:
            curr_y -= 1

        else: #
            flag = False

    return False

    

for _ in range(10):
    test_case = int(input())

    # 배열 생성
    arr = [list(map(int, input().split())) for _ in range(100)]

    for y in range(100):
        if arr[0][y] == 1:
            visited = [[0]*100 for _ in range(100)]

            curr_x  = 0
            curr_y = y

            while curr_x < 99:
                visited[curr_x][curr_y] = 1

                # 왼쪽 길 있으면
                if curr_y > 0 and arr[curr_x][curr_y - 1] == 1:
                    curr_y -= 1

                # 오른쪽 길 있으면
                elif curr_y < 99 and arr[curr_x][curr_y+1] == 1:
                    curr_y += 1
                else:
                    curr_x += 1

            if arr[curr_x][curr_y] == 2:
                result = y
                break

    print(f'{test_case} {result}')