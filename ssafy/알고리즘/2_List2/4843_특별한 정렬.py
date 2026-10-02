T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_arr = []

    while arr:
        max_num = max(arr)
        new_arr.append(max_num)
        arr.pop(arr.index(max_num))
        min_num = min(arr)
        new_arr.append(min_num)
        arr.pop(arr.index(min_num))

    print(f'#{tc}', *new_arr[:10])
        