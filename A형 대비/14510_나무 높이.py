'''
N개의 나무


'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    max_height = max(trees) # 최대 높이
    one = 0
    two = 0

    for tree in trees:
        diff = max_height - tree # 최대 높이와 현재 나무 높이의 차이 구하기

        one += diff%2
        two += diff//2

    while two > one+1:
        two -= 1
        one += 2

    if one > two:
        answer = one*2 - 1
    else:
        answer = two*2

    print(f'#{tc} {answer}')
