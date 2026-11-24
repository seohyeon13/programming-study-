from collections import deque

N, M = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N+1)] # 인접 리스트 (어떤 노드들이 연결되어 있는지)
indegree = [0]*(N+1) # 진입 차수

for i in range(M):
    a = students[i][0]
    b = students[i][1]

    adj_list[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, N+1):
    if not indegree[i]:
        q.append(i)

answer = []

while q:
    cur = q.popleft()
    answer.append(cur)

    for next in adj_list[cur]:
        indegree[next] -=1

        if not indegree[next]:
            q.append(next)

print(*answer)
