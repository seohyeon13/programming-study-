'''
순위가 바뀐 팀 목록 주어졌을 때
올해 순위를 만드는 프로그램 작성

*확실한 올해 순위 만들 수 없는 경우 o
*일관성 없는 잘못된 정보일 수 O

'''
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input()) # 팀의 수
    last_year = list(map(int, input().split())) # 작년 팀

    m = int(input()) # 등수가 바뀐 쌍의 수

    now = [] # 현재 등수 저장
    adj_list = [[] for _ in range(n+1)] # 인접 리스트 -> 연결관계
    indegree = [0]*(n+1) # 차수 -> 내 노드로 몇개가 들어오는지
    # 1. 작년 순위 인접리스트, 차수 저장
    for i in range(n):
        for j in range(i+1, n):
            a = last_year[i]
            b = last_year[j]

            adj_list[a].append(b)
            indegree[b] += 1

    # 2. 순위 바뀐거 저장
    for _ in range(m):
        a, b = map(int, input().split())

        if a in adj_list[b]:
            adj_list[b].remove(a)
            adj_list[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1

        else:
            adj_list[a].remove(b)
            adj_list[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
    q = deque()

    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)

    uncertain = False

    while q:
        if len(q) > 1:
            uncertain = True

        node = q.popleft()
        now.append(node)

        for next_node in adj_list[node]: # 현재 노드와의 연결관계
            indegree[next_node] -= 1

            if not indegree[next_node]:
                q.append(next_node)

    if len(now) != n:
        print('IMPOSSIBLE')
    elif uncertain:
        print('?')
    else:
        print(*now)
    



    