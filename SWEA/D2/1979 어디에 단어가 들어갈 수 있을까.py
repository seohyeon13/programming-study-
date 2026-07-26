T = int(input())

for test_case in range(1, T + 1):

    # N : 가로 세로 길이
    # k : 단어의 길이
    N, K = map(int, input().split())

    arr = []

    # 퍼즐 모양 입력 
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # 1 : 흰
    # 0 : 검
    cnt = 0

    for i in range(N):
        cnt_white = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_white +=1

            else:
                if cnt_white == K:
                    cnt += 1
                    cnt_white = 0
        if cnt_white == K:
            cnt+=1

    for i in range(N):
        cnt_white = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_white +=1

            else:
                if cnt_white == K:
                    cnt += 1
                    cnt_white = 0
        if cnt_white == K:
            cnt+=1

    print(f'#{test_case} {cnt}')