T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0

    if N > M:
        A, B = B, A
        N,M = M,N

    answer = 0

    for i in range(M-N+1):
        sum = 0

        for j in range(N):
            sum += A[j]*B[i+j]
        answer = max(answer, sum)

    print(f'#{tc} {answer}')