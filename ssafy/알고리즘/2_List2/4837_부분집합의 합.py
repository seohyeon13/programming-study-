T = int(input())
def dfs(num):
    global answer
    # 종료 조건
    if len(combination) == N and sum(combination) == K:
        answer += 1
        return
    
    for i in range(num,13):
        combination.append(i)
        dfs(i+1)
        combination.pop()

for tc in range(1, T+1):
    # N : 부분집합 원소 수, K : 부분 집합의 합
    N, K = map(int, input().split())
    answer = 0
    combination = []
    dfs(1)

    print(f'#{tc} {answer}')