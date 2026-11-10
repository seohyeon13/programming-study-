arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def print_name():
    print('{', end = ' ')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end = ' ')
    print('}')
def dfs(count):
    if count == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        dfs(count+1)
        path.pop()

dfs(0)