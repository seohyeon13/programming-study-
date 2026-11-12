cnt_com = int(input()) # 컴퓨터의 수

couple = int(input()) # 연결되어 있는 쌍의 수

mat = [[0]*(cnt_com+1) for i in range(cnt_com+1)]

for i in range(couple):
    a, b = map(int, input().split())
    mat[a][b] = 1
    mat[b][a] = 1

virus = []
visited = [0] * (cnt_com+1)

def dfs(mat, visited, start):
    stack = [start]

    while stack:
        num = stack.pop()

        if visited[num] == 0:
            visited[num] = 1
            
            if num not in virus:
                virus.append(num)
        
        for i in range(cnt_com, 0, -1):
            if mat[num][i] == 1 and visited[i] == 0:
                stack.append(i)


dfs(mat, visited, 1)

print(len(virus)-1)

