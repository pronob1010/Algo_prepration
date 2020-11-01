def isValid(arr,x,y,pos):
    for j in range(len(arr)):
        if arr[x][j]==pos:
            return False

    for i in range(len(arr)):
        if arr[i][y]==pos:
            return False


    sub_l_top_i = 3*(x//3)
    sub_l_top_j = 3*(y//3)
    for i in range(3):
        for j in range(3):
            if arr[sub_l_top_i+i][sub_l_top_j+j] == pos:
                return False
    return True



def solveSudoku(arr, i, j):
    if i == len(arr):
        print(arr)
        return arr
    else:
        nx_i = 0
        nx_j = 0

        if j == len(arr)-1:
            nx_i = i+1
            nx_j = 0
        else:
            nx_i = i
            nx_j = j+1

        if arr[i][j] != 0:
            solveSudoku(arr,nx_i,nx_j)
        else:
            for pos in range(1, len(arr)+1):
                if isValid(arr,i,j, pos):
                    arr[i][j] = pos
                    solveSudoku(arr, nx_i, nx_j)
                    arr[i][j] = 0

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))[:n]
    arr.append(row)
solveSudoku(arr, 0, 0)




















# def isValid(arr, x, y, posOption):
#     for j in range(len(arr)):
#         if arr[x][j]== posOption:
#             return False
#     for i in range(len(arr)):
#         if arr[i][y] == posOption:
#             return False
#
#     Sub_mat_topLeft_i = 3*(x//3)
#     Sub_mat_topLeft_j = 3*(y//3)
#     for i in range(3):
#         for j in range(3):
#             if arr[Sub_mat_topLeft_i+i][Sub_mat_topLeft_j+j] == posOption:
#                 return False
#
#     return True
#
#
# def solveSudoku(arr, i , j):
#     if i == len(arr):
#         for i in arr:
#             print(*i, sep=" ")
#         return arr
#
#     else:
#         next_i = 0
#         next_j = 0
#
#         if j== len(arr)-1:
#             next_i = i+1
#             next_j = 0
#         else:
#             next_i = i
#             next_j = j+1
#
#         if arr[i][j] != 0:
#             solveSudoku(arr,next_i,next_j)
#         else:
#             for posOption in range(1,n+1):
#                 if isValid(arr, i, j, posOption):
#                     arr[i][j] = posOption
#                     solveSudoku(arr, next_i, next_j)
#                     arr[i][j] = 0
#
#
# n = int(input())
# arr = []
# for i in range(n):
#     row = list(map(int, input().split()))[:n]
#     arr.append(row)
#
#
# solveSudoku(arr, 0, 0)
#
# # p = []
# # p = solveSudoku(arr,0,0)
# # for i in p:
# #     print(*i, sep=" ")
#
# #
# # for i in arr2:
# #     print(*arr2[i], sep=" ")
#
#
9
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
#
#
#
