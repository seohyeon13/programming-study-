'''
1. 자치구 나누기
2. 연결되어있는지 확인
3. 차이 최소값 구하기
'''
from collections import deque

T = int(input())

def bfs(group):
    visited = [0]*(N+1)
    q = deque()

    start = group[0]

    visited[start] = 1
    q.append(start)

    count = 1

    while q:
        cur = q.popleft()

        for n in adj_list[cur]:
            if n not in group:
                continue

            if visited[n]:
                continue

            visited[n] = 1
            count+=1
            q.append(n)

    return count == len(group)
    
for tc in range(1, T+1):
    N = int(input()) # 행성 수

    # n+1개
    people =[0] + list(map(int, input().split()))


    adj_list = [[] for _ in range(N+1)]

    for planet in range(1, N+1):
        row = list(map(int, input().split()))

        k = row[0] # 연결된 갯수

        for i in range(1, k+1):
            adj_list[planet].append(row[i])

    answer = float('inf')

    for mask in range(1, (1<<N)-1): # 행성 갯수만큼 표현
        alpha = []
        beta = []

        sum_alpha = 0
        sum_beta = 0

        for planet in range(1, N+1): # 각 행성 1부터 N까지 있으므로
            if mask & (1 << (planet -1)): # 1번 행성 위치가 0번 비트 위치니까.
                alpha.append(planet) # 1이면 alpha
                sum_alpha += people[planet]
            else: # 베타
                beta.append(planet)
                sum_beta += people[planet]

        if not bfs(alpha): # alpha 연결되지 않았다면. bfs(alpha) return 0
            continue
        if not bfs(beta):
            continue

        difference = abs(sum_alpha - sum_beta)
        answer = min(answer, difference)

    if answer == float('inf'): # 아무것도 찾지 못한 경우
        answer = -1

    print(f'#{tc} {answer}')