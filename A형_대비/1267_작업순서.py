from collections import deque

for tc in range(1, 11):
    # V : 정점 개수
    # E : 간선 개수
    V, E = map(int,input().split())

    # 간선 나열 -> 간선을 이루는 두 정점
    # 홀수번째 -> 짝수번째로 연결
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    # 들어오는 간선 저장용
    node_list = [0]*(V+1) 
    
    # 인접 리스트에 인접 정점 저장
    # 연결 관계 저장
    for i in range(0, E*2, 2):
        node1 = arr[i]
        node2 = arr[i+1]
        adj_list[node1].append(node2)
        node_list[node2] += 1

    q = deque()
    # 들어오는 간선이 0인 노드들 q에 넣기
    for i in range(1, V+1):
        if not node_list[i]:
            q.append(i)
    answer = []

    while q:
        num = q.popleft()
        answer.append(num)

        for n in adj_list[num]:
            node_list[n] -= 1
            if node_list[n] == 0:
                q.append(n)
    print(f'#{tc}', *answer)
        


        
    


        

