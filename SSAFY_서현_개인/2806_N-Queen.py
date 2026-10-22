T = int(input())

def check_queens(row, col):
    if col_list[col] != -1:
        return 0

    for c in range(N):
        if col_list[c] != -1:
            r = col_list[c]

            if abs(row-r) == abs(col-c):
                return 0

    return 1

def queen(row, queens_cnt):
    global answer
    if queens_cnt == 0:
        answer += 1
        return

    for j in range(N):
        if check_queens(row, j):
            col_list[j] = row
            queen(row+1, queens_cnt-1)

            col_list[j] = -1
        
    

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    col_list = [-1]*N

    queen(0, N)

    print(f'#{tc} {answer}')