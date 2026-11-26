import heapq

# N : 문제의 수
# M :먼저 푸는 것이 좋은 문제에 대한 정보 개수
N, M = map(int, input().split())

problems = [list(map(int, input().split())) for _ in range(M)]

indegree = [0]*(N+1)
adj_list = [[] for _ in range(N+1)]

for i in range(M):
    a = problems[i][0]
    b = problems[i][1]

    adj_list[a].append(b)
    indegree[b]+=1
    
q = []

for i in range(1, N+1):
    if not indegree[i]:
        heapq.heappush(q, i)

answer = [] 

while q:
    node = heapq.heappop(q)
    answer.append(node)

    for next_node in adj_list[node]:
        indegree[next_node] -= 1

        if not indegree[next_node]:
            heapq.heappush(q, next_node)

print(*answer)
