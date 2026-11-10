a = [1,2,3,4,5]
comb_list = []
def dfs(count, idx):
    if count == 2:
        print(*comb_list)
        return

    for i in range(idx, 5):
        comb_list.append(a[i])
        dfs(count+1, i+1)
        comb_list.pop()
dfs(0,0)

# numbers = [1,2,3,4]
# M = 2
# pick_numbers = []
# cases = []

# # 1. 중복 순열
# def perm1(count):
#     if count == M:
#         print(pick_numbers)
#         return

#     for i in range(len(numbers)):
#         pick_numbers.append(numbers[i])
#         perm1(count+1)
#         pick_numbers.pop()

#     # return None
# # perm1(0)

# # 2. 조합
# def comb1(count, idx):
#     if count == M:
#         print(pick_numbers)
#         return

#     for i in range(idx, len(numbers)):
#         pick_numbers.append(numbers[i])
#         comb1(count+1, i+1)
#         pick_numbers.pop()

# # comb1(0, 0)

# # 3. 중복 조합
# def comb2(count, idx):
#     if count == M:
#         print(pick_numbers)
#         return

#     for i in range(idx, len(numbers)):
#         pick_numbers.append(numbers[i])
#         comb2(count+1, i)
#         pick_numbers.pop()

# # comb2(0, 0)

# # 4. 순열 > 방문 배열
# visited = [0]*len(numbers)

# def perm2(count):
#     if count == M:
#         cases.append(pick_numbers[:])
#         print(pick_numbers)
#         return

#     for i in range(len(numbers)):
#         if visited[i]: # 1이 적혀있다면? True 처리
#             continue

#         pick_numbers.append(numbers[i])
#         visited[i] = 1
#         perm2(count+1)
#         pick_numbers.pop()
#         visited[i] = 0

# perm2(0)

# print(cases)