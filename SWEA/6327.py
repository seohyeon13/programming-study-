def squre(a):
    return a**2

n1, n2 = input().split(', ')

n1 = int(n1)
n2 = int(n2)
print(f"square({n1}) => {squre(n1)}")
print(f"square({n2}) => {squre(n2)}")