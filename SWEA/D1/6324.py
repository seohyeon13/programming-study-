def duplication_list(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            arr2.append(i)

arr1 = [1,2,3,4,3,2,1]
print(arr1)

arr2 = []
duplication_list(arr1, arr2)
print(arr2)