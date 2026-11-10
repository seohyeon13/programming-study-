from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())

    arr = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]

    indegree = [0] * (V+1)

    for i in range(0, E*2, 2):
        a = arr[i]
        b = arr[i+1]

        graph[a].append(b)
        indegree[b]+=1

    q = deque()

    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)

    answer = []

    while q:
        now = q.popleft()
        answer.append(now)

        for next_node in graph[now]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

    print(f'#{tc}', *answer)
    