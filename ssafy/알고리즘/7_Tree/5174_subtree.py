'''
부모 없는 노드 -> 전체 루트 노드
부모 노드를 인덱스로 한다.
자식 노드가 0 -> 노드가 자식없는 경우
1번 인덱스 -> 6 : 6번 노드의 부모가 1번 노드
  1
 /
6

E : 간선 개수
N : 루트 노드
tree 리스트 : E개의 (부모, 자식) 노드 번호 쌍
노드 번호 : 1번부터 E+1번까지 존재

구해야 하는 것 : 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
'''
def create_tree():
    for i in range(0, len(arr), 2):
        parent = arr[i]
        if not left[parent]: # 왼쪽 자식 없으면
            left[parent] = arr[i+1]
        else:
            right[parent] = arr[i+1]

def search_tree(root):
    global answer
    answer += 1
    if left[root]:
        search_tree(left[root])
    if right[root]:
        search_tree(right[root])


T=int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    right = [0]*(E+2) # 트리 리스트 생성
    left = [0]*(E+2)
    answer = 0
    create_tree()
    search_tree(N)


    print(f'#{tc} {answer}')