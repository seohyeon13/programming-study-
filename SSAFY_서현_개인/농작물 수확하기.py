# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
     
#     N = int(input()) # 농장의 크기
 
#     arr = []
#     sum_arr = 0 
 
#     for i in range(N):
#         row = list(map(int, input()))
#         arr.append(row)
 
#     for i in range(N):
#         #y = N//2 # 2
         
#         center = N//2 #2
#         y = abs(center-i) # 0행 -> 2, 1행 -> 1, 2행 -> 0
#         y_2 = N-y # 0행 -> 3, 1행 -> 4, 2행 -> 5
 
#         for j in range(y, y_2):
             
#             sum_arr += arr[i][j]
 
     
#     print(f'#{test_case} {sum_arr}')

# ======================================================
# 강사님 풀이
# 입력 먼저 봄
# <파스칼 삼각형> - 정석 풀이

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     pascal_tri = []

#     # r : 0 ~ N-1층
#     for r in range(N):
#         row = []

#         for c in range(r+1):
#             if c== 0 or c == r:
#                 row.append(1)
#             else:
#                 row.append(pascal_tri[r-1][c-1] + pascal_tri[r-1][c])
#         pascal_tri.append(row)

#     print(f'#{tc}')

#     for r in range(N):
#         print(*pascal_tri[r])


# ========================================================
# # 바로 위 행만 저장하면 되는데, 위에 코드는 다 저장하고 있음 -> 즉 메모리 효율적이지 못함

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     print(f'#{tc}')

#     # r : 0 ~ N-1층
#     before_row = []
#     for r in range(N):
#         row = []

#         for c in range(r+1):
#             if c== 0 or c == r:
#                 row.append(1)
#             else:
#                 row.append(before_row[c-1] + before_row[c])

#         print(*row)
#         before_row.append(row)

# ==============================================================
# 3번째 풀이 -> 10개층이 최대니까 첨부터 다 만들어놓고 해당층ㅁ만 찍어내면 됨
