'''
N : 식재료 수
foods : list => N*N개의 시너지 값
food_count : N/2개 음식 만들기
food_A = foods[i][j] + food[j][i]
food_B = foods[i][j] + food[j][i]

diff = food_A - food_B => 두 음식의 맛 차이

N개 중에 조합 뽑기
해당 조합으로 같이 요리했을 때의시너지 계산
최소인 것 -> answer에 저장


'''
def cal():
    global answer
    not_comb = []
    sum_A, sum_B = 0, 0
    for i in range(N):
        if i not in comb_list:
            not_comb.append(i)

    for i in comb_list:
        for j in comb_list:
            sum_A += foods[i][j]

    for i in not_comb:
        for j in not_comb:
            sum_B += foods[i][j]

    answer = min(answer, abs(sum_A - sum_B))
    
def dfs(count, idx):
    if count == N//2:
        cal()
        return

    for i in range(idx, N):
        comb_list.append(i)
        dfs(count+1, i+1)
        comb_list.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf') # 최소값 저장
    comb_list = []

    dfs(0,0) # 재료 조합 선택 

    print(f'#{tc} {answer}')