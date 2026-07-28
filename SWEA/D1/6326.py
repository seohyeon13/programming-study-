def factorial(a):
    num = 1
    for i in range(a, 0, -1):
        num *=i
    return num

num = int(input())

print(factorial(num))