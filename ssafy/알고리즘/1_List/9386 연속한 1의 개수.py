T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수열의 길이
    numbers = list(input())
    answer = 0
    cnt = 0

    for number in numbers:
        if number == '1':
            cnt += 1
            answer = max(answer, cnt)
        else:
            cnt = 0

    print(f'#{tc} {answer}')