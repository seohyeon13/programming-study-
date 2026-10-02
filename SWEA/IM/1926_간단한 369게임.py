N = int(input())

for i in range(1, N+1):
    number = str(i)
    cnt = 0

    for n in number:
        if n in '369':
            cnt += 1

    if cnt > 0:
        print('-'*cnt, end = ' ')
    else:
        print(i, end = ' ')
