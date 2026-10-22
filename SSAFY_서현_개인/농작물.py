# 마름모 -> 중앙으로부터 거리 똑같음

# T = int(input())

# for tc in range(1, T+1):
#     answer = 0

#     N = int(input())
#     # 어차피 농작물 안바꿈
#     crops = [ input() for _ in range(N)]

#     mid = distance = N//2 # 이 거리 이내
    
#     for r in range(N):
#         for c in range(N):
#             if abs(mid-r) + abs(mid-c) <= distance:
#                 answer += int(crops[r][c])


#     print(f'#{tc} {answer}')

# ===========================================
# 늘어났다가 줄어드네? 언제까지 늘어나는거야?

T = int(input())

for tc in range(1, T+1):
    answer = 0

    N = int(input())
    # 어차피 농작물 안바꿈
    crops = [ input() for _ in range(N)]

    mid = distance = N//2 # 이 거리 이내
    
    for r in range(N):
        for c in range((abs(mid-r)), (abs(mid-r))+N-2*(abs(mid-r))):
            if abs(mid-r) + abs(mid-c) <= distance:
                answer += int(crops[r][c])


    print(f'#{tc} {answer}')