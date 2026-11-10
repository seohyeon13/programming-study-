T = int(input())

for tc in range(1, T+1):
    N=float(input())

    answer = ''

    while N>0 and len(answer) <13:
        N*=2
        if N >= 1:
            answer += '1'
            N -= 1
        else:
            answer+='0'

    if N > 0:
        answer = 'overflow'

    print(f'#{tc} {answer}')

