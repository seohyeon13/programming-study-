def rotation(arr):
    new_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]

    return new_arr


T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    # 90도
    arr2 = rotation(arr)

    # 180도
    arr3 = rotation(arr2)    

    # 270도
    arr4 = rotation(arr3)

    print(f'#{test_case}')

    for i in range(N):
        print(''.join(map(str,arr2[i])), end = ' ')
        print(''.join(map(str,arr3[i])), end = ' ')
        print(''.join(map(str,arr4[i])))