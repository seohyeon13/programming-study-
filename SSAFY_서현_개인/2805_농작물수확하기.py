T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    answer = 0
    for i in range(N):
        center = N//2 
        col = abs(center-i)
        col2 = N-col 

        for j in range(col, col2):
            answer += farm[i][j]

    
    print(f'#{tc} {answer}')