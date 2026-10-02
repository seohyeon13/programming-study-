T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(input().split())
    numbers.sort()
    print(f'#{tc}', *numbers)

