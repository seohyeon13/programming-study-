T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def dfs(root):
    global cnt
    cnt += 1

    for child in ls[root]: # 6
        dfs(child)

for test_case in range(1, T + 1):
    E, N = map(int, input().split())

    #(간선갯수) E=5, N = 1
    
    # 인덱스가 짝수 -> 부모
    # 인덱스가 홀수 -> 자식

    couple = list(map(int, input().split()))

    ls = [[] for i in range(E+2)]# 부모 자식 저장 리스트


    for i in range(0,len(couple),2):
        parent = couple[i]
        child = couple[i+1]

        ls[parent].append(child)

    #root = ls[N] #1 
    cnt = 0

    dfs(N)
    
    print(f'#{test_case} {cnt}')
