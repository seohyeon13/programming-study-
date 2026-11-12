from collections import deque

# N : 정점 개수, M : 간선 개수, V : 시작 정점 
N, M, V = map(int, input().split())

# 1. 인접 행렬 풀이
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M): # 간선 갯수만큼 반복
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# dfs 1 : 재귀
def dfs(start_node):
    visited_dfs[start_node] = 1 # 방문 처리
    print(start_node, end = ' ') # 출력

    for i in range(1, N+1): # 시작노드와 연결된 다른 노드 살펴보기
        if arr[start_node][i] == 1 and visited_dfs[i] == 0:
            dfs(i)

# dfs 2 : 스택
def dfs2(start_node):
    stack = [start_node]

    while stack:
         curr_node = stack.pop() # 스택에서 하나 빼오기

         if visited_dfs[curr_node]: # 이미 방문했으면
             continue
             
         visited_dfs[curr_node] = 1

         print(curr_node, end = ' ')

         for i in range(N, 0, -1):
             if arr[curr_node][i] ==1 and visited_dfs[i] == 0:
                 stack.append(i)
                 
             
def bfs(start_node):
    q = deque() # 큐 생성
    q.append(start_node)
    visited_bfs[start_node] = 1

    while q: # 큐가 있을 때까지
        curr_node = q.popleft() # 큐에서 빼오기
        print(curr_node, end = ' ')

        for i in range(1, N+1):
            if arr[curr_node][i] == 1 and visited_bfs[i] == 0:
                q.append(i)
                visited_bfs[i] = 1 # 방문 처리


visited_dfs = [0]*(N+1)
dfs2(V)

print()

visited_bfs = [0]*(N+1)
bfs(V)

