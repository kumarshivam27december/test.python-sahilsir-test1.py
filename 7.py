# # '''
# # 5 4 3 2 1 
# # 4 3 2 1 
# # 3 2 1
# # 2 1
# # 1
# # '''

# # # for i in 
# # # n=5
# # # for i in range(n+1,1):
# # #     for j in range(n+1,i):
# # #         print(i,end=" ")
# # #     print()

# # n=int(input())

# # for i in range(n,0,-1):

# #     j=i

# # while j>0:

# #     print(j,end='')

# # j=j-1

# # print()

# # # If you want a output like :

# # # ‘’’

# # # 543214321321211

# # # ‘’’

# # # Then the code for the above output is :

# # n=int(input())

# # for i in range(n,0,-1):

# #     j=i

# # while j>0:
# #     print(j,end='')

# # j=j-1


# rows = 5
# # reverse loop
# for i in range(rows, 0, -1):
#     num = i
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

