T = int(input())

def dfs(count):
    global answer
    if count == N:
        answer += 1
        return

    for i in range(N): # 열 순회
        if i in visited_col: # 이미 들어있으면
            continue
        # 대각검사
        for row in range(count):
            if count-row == abs(i-col[row]):
                break
        else:
            col[count] = i
            visited_col.add(i)
            dfs(count+1)
            visited_col.remove(i)

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    col = [-1]*N # 대각검사, 해당 행에 어떤 열에 놓았는지 확인
    visited_col = set() # 들어있는 열 선택 못함
    dfs(0)
    print(f'#{tc} {answer}')