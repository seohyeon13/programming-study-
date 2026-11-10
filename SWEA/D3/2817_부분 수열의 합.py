T = int(input())

def dfs(idx, sum):
    global answer
    if sum > K:
        return
    if sum == K:
        answer += 1
        return
    for i in range(idx, len(arr)):
        sum+=arr[i]
        dfs(i+1,sum)
        sum-=arr[i]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    answer = 0
    dfs(0, sum)
    print(f'#{tc} {answer}')