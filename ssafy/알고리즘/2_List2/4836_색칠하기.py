T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0: # 아무것도 안칠해져있을 경우
                    arr[i][j] = color
                elif arr[i][j]!=0: # 색이 칠해져 있을 경우
                    arr[i][j] = -1
    answer = 0
    for row in arr:
        answer += row.count(-1)

    print(f'#{tc} {answer}')
        

