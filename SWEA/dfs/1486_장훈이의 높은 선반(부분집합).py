T =int(input())

def dfs(idx, height):
    global ans
    if height >= B:
        ans = min(ans, height-B)
        return

    if idx == N:
        return
    dfs(idx+1, height)
    dfs(idx+1, height+S[idx])
        
for tc in range(1, T+1):
    N, B = map(int, input().split())

    S = list(map(int, input().split()))
    ans = float('inf')
    dfs(0, 0)
    print(f'#{tc} {ans}')