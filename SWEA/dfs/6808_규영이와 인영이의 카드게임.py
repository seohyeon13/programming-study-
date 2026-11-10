'''
1~18 카드
9장씩 카드 나눔
9라운드까지
각 라운드 -> 카드 한장씩 비교 -> 점수 계산
높은 수가 적힌 카드 -> 카드에 적힌 수의 합만큼 점수 얻음
낮은 수가 적힌 카드 -> 0점
9라운드까지 끝내 후 총점 비교 -> 더 높은 사람이 이김
총점 같으면 무승부

규영이가 이기는 경우의수, 지는 경우의 수 구하기

'''
T = int(input())

def card_game():
    global win, lose
    score = [0,0] # 0번 : 규영, 1번 : 인영
    for i in range(9):
        if numbers[i] > combination[i]:
            score[0] += (numbers[i]+combination[i])
        else:
            score[1] += (numbers[i]+combination[i])

    if score[0] > score[1]:
        win += 1
    else:
        lose += 1
    
def dfs(count):
    if count == 9:
        card_game()# 점수 계산
        return

    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            combination.append(numbers2[i])
            dfs(count+1)
            combination.pop()
            visited[i] = 0

    
for tc in range(1, T+1):
    # 규영이가 가지고 있는 카드 
    numbers = list(map(int, input().split()))
    # 인영이가 가지고 있는 카드
    numbers2 = []
    for i in range(1, 19):
        if i not in numbers:
            numbers2.append(i)
    combination = []
    win = 0
    lose = 0
    visited = [0]*9
    dfs(0) # 인영이가 가진 카드 순서 계산

    print(f'#{tc} {win} {lose}')

    

    



