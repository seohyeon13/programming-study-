def select_hamburger(idx, total_score, total_kcal):
    global max_score

    # 지금까지 더한 칼로리가 제한 칼로리보다 크면 리턴
    if total_kcal > L:
        return
    # 높은 점수 반영
    if max_score < total_score:
        max_score = total_score

    # 점수, 칼로리가 기록된 리스트에서 하나씩 꺼내옴
    for i in range(idx, len(score_kcal)):
        # 점수 저장
        total_score += score_kcal[i][0]
        total_kcal += score_kcal[i][1]
        select_hamburger(i+1, total_score, total_kcal)
        total_score -= score_kcal[i][0]
        total_kcal -= score_kcal[i][1]


T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split()) # 재료 수, 제한 칼로리

    score_kcal = [list(map(int, input().split())) for _ in range(N)] # 맛에 대한 점수, 칼로리

    max_score = float('-inf')

    select_hamburger(0, 0, 0)

    print(f'#{test_case} {max_score}')