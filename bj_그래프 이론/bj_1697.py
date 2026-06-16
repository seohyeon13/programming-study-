from collections import deque

N, K = map(int, input().split())

q = deque()

visited = [0] * (1000000+1)

def bfs(start):
    q.append(start)
    visited[start] = 1
    #print(start)
    while q:
        x = q.popleft()
        #print(x)

        if x == K:
            return visited[K]

        for i in (x-1, x+1, 2*x):
            if 0<=i<=100000:
                if visited[i] == 0 :
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs(N) 

print(visited[K]-1)

        


