T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    height1 = list(map(int, input().split()))
    height2 = list(map(int, input().split()))

    best1 = height1[0]
    best2 = height2[0]

    for i in range(1, N):
        next1 = max(best1 + (height1[i]-P), best2 + height1[i])
        next2 = max(best2 + (height2[i]-P), best1+height2[i])

        best1, best2 = next1, next2

    print(f'#{tc} {max(best1, best2)}')