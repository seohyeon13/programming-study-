'''
제한 칼로리 이하의 조합 중
맛에 대한 점수가 높은 햄버거의 점수
============================
칼로리 확인 해야 함. L보다 안크도록
count -> 재료의 수 -> 칼로리에 의존.

'''
T = int(input())

def dfs(count, score, kcal):
    global answer
    if kcal>L:
        return

    answer = max(answer, score)
    
    for i in range(count,N):
        dfs(i+1, score+arr[i][0], kcal+arr[i][1])
        
        
for tc in range(1, T+1):
    # N : 재료의 수, K : 제한 칼로리
    N, L = map(int, input().split())
    # 점수, 칼로리 
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, 0)
    print(f'#{tc} {answer}')

    