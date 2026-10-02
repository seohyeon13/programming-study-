'''
1 ~ N : 이진 탐색 트리에 저장
왼쪽 섭트 루트 < 현재 노드 < 오른쪽 섭트 루트 (규칙 항상 만족)
완전 이진 트리 -> 효울적인 이진 탐색 트리

루트 = 1번

구해야 하는 것 : 루트에 저장된 값, N/2번 노드에 저장된 값 

N = 6
1,2,3,4,5,6

'''
def create_tree():
    
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    create_tree()

    print(f'#{tc} {answer}')