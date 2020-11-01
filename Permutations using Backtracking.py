def permutation(arr, current_item, total_item):
    if current_item>total_item:
        print(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = current_item
            permutation(arr, current_item+1, total_item)
            arr[i] = 0


n = int(input())
r = int(input())

arr = [0]*n
permutation(arr, 1, r)