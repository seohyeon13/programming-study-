T = int(input())

def dfs(balloons):
    # 1. balloons의 길이가 1 (1개 남았을 때)
    # 자기 자신 값 리턴
    if len(balloons) == 1:
        return balloons[0]
    # 2. balloons 길이 여러개라면
    # 현재 해당하는 숫자 조합의 점수가 이미 존재하는지 확인
    if set(balloons) in memo:
        return memo[set(balloons)]

    # 3. 그것도 아니라면, 점수 계산
    for i in range(len(balloons)):
        if i == 0: # 맨 오른쪽이면 왼쪽 값 리턴
            score = balloons[i+1]
        elif i == (len(balloons)-1): # 맨 뒤
            score = balloons[i-1]
        else:
            score = balloons[i-1]*balloons[i+1]

        remaining = balloons.copy()
        remaining.pop(i)

        total_score = score + dfs(remaining)

        max_score = max(max_score, total_score)

    memo[set(balloons)] = max_score

    return max_score

for tc in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split()))
    answer = float('-inf')
    memo = {}
    dfs(balloons)
    print(f'#{tc} {answer}')

    '''
    07:50:27 (Runtime error)
Error Message:
Memory error occurred, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
    '''