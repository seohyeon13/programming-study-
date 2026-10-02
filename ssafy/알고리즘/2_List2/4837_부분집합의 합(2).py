T = int(input())

for tc in range(1, T+1):
    # N : 부분집합 원소의 수, K : 부분집합의 합
    N, K = map(int, input().split())
    arr = list(range(1,13))
    answer = 0
    for i in range(1<<12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1<<j):
                cnt+=1
                total += arr[j]
        if cnt == N and total == K:
            answer += 1
    print(f'#{tc} {answer}')