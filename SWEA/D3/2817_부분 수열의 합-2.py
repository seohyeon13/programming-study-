T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N개의 수열
    arr = list(map(int, input().split()))
    
    answer = 0

    for i in range(1<<N):
        sum = 0
        for j in range(N):
            if i & (1<<j):
                sum+=arr[j]
            if sum > K:
                break
        if sum == K:
            answer += 1
    
    print(f'#{tc} {answer}')