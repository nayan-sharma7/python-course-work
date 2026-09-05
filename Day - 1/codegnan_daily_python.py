# # # n = 3
# # # for r in range(n):
# # #     for c in range(n-r):
# # #         print("*",end=" ")
# # #     print()

# n = 3 
# for r in range(n):
#     for c in range(n-r):
#         print(" ",end=" ")
#     for c in range(2*r+1):
#         print("*",end=" ")
#     print()

# n = 3
# for r in range(n):
#     #spaces
#     for c in range(r):
#         print(" ",end=" ")
#     #stars
#     for c in range(2*n-(2*r+1)):
#         print("*",end=" ")
#     print()

# n = 3 
# for r in range(n):
#     #spaces
#     for c in range(n-r-1):
#         print(" ",end=" ")
#     #stars
#     for c in range(2*r+1):
#         print("*")

# num =1      
# n = 3 
# for r in range(n):
#     for c in range(n-r):
#         print(" ",end=" ")
#     for c in range(2*r+1):
#         print(num,end=" ")
#         num+=1
#     print()

# for r in range(4):
#     for c in range(4):
#         if r==0 or r==3 or c==0 or c==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# name = "Nayansharma"
# for i in range(1,len(name)+1):
#     print(name[i-1]*i)

# char = 65 
# for r in range(4):
#     for c in range(4):

d1,d2=0,0
m = [[10,20,30,40],[30,60,70,80],[90,100,200,300],[400,500,600,700]]
for r in range(len(m)):
    for c in range(len(m[0])):
        if r == c:
            d1 += m[r][c]
        elif (r+c)==(len(m)-1):
            d2 +=m[r][c]
print(d1,d2)
print(abs(d1-d2))