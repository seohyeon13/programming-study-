T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 행 검사
    for i in range(9):
        row = set(arr[i])

        if len(row) != 9:
            result = 0
            break

    # 열 검사
    for j in range(9):
        col = set()

        for i in range(9):
            col.add(arr[i][j])

        if len(col) != 9:
            result = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            matrix = set()

            for x in range(i, i+3):
                for y in range(j, j+3):
                    matrix.add(arr[x][y])

            if len(matrix) != 9:
                result = 0
                break
        # if result == 0:
        #     break
    
    print(f'#{test_case} {result}')

        

    
