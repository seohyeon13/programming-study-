for _ in range(10):
    test_case = int(input())

    arr = [list(map(int,input().split)) for _ in range(100)] # 전체 배열 입력받기

    dx = [1, 0, 0] # 하 우 좌
    dy = [0, 1, -1]

    result = 0

    for i in range(100): # 첫번째 행 열 하나씩
        if arr[0][i] == 1:
            curr_x = 0
            curr_y = i

            dir = 0

            while curr_x < 99:
                if dir == 0:
                    pass

