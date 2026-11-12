# union-find : 각각의 독립된 data를 그룹화해서 관리하기 위해 
# arr 배열 값은 해당 인덱스의 boss가 누구인지 나타냄
# union(0,1) -> 0이 속한 그룹과 1이 속한 그룹이 하나로 합쳐짐
# 0이 속한 그룹의 그룹장이라고 한다면 -> 인덱스 1의 값을 0으로 바꾸기

arr = [ i for i in range(6)]
rank = [0]*6

def find_boss(member):
    if arr[member] == member: # 자기 자신이 보스라면(그 그룹의 보스 찾음)
        return member

    ret = find_boss(arr[member]) # 보스가 아니라면 arr배열의 값을 가지고 보스 찾기
    arr[member] = ret # 경로 단축 코드
    return ret

def union(a, b):
    fa = find_boss(a)
    fb = find_boss(b)
    if fa == fb: # 두 보스가 같으면 이미 같은 그룹
        return
    if rank[a] == rank[b]:
        rank[a] += 1
        arr[fb] = fa
    elif rank[a]>rank[b]:
        arr[fb] = fa
    else:
        arr[fa] = fb
    
    arr[fb] = fa # 보스가 다르면 a의 보스가 통합 장
union(0,1)
union(3,4)
union(1,4)
union(1,3)
union(5,4)