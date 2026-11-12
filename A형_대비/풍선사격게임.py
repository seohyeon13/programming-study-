T = int(input())

def dfs(balloons, memo):
    if len(balloons) == 0:
        return 0
    if len(balloons) == 1:
        return balloons[0]

    best = float('-inf')
    n = len(balloons)
    for i in range(n):
        # i번째 풍선을 터뜨릴 때 얻는 점수
        if i == 0:
            score = balloons[i + 1]
        elif i == n - 1:
            score = balloons[i - 1]
        else:
            score = balloons[i - 1] * balloons[i + 1]

        # i번째 풍선을 빼고, 남은 풍선의 최대 점수를 구함
        remaining = balloons[:i] + balloons[i + 1:]
        total = score + dfs(remaining, memo)

        best = max(best, total)

    # 이번 상태에서 모든 선택을 비교한 뒤 최댓값 저장
    memo[balloons] = best
    return best       


for tc in range(1, T+1):
    N = int(input())

    balloons = list(map(int, input().split()))

    memo = {}

    answer = dfs(balloons, memo)

    print(f'#{tc} {answer}')