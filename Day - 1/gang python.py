# # # l = [-2,-77,74,0,7,18,18,33,74,34]
# # # first = second = float('-inf')
# # # for num in l:
# # #     if num > first:
# # #         second = first 
# # #         first = num
# # #     elif num>second and num<first:
# # #         second = num
# # # print(first)
# # # print(second)


# # # l = [1,1,1,2,2,2,3,3,3,0,1,1,-1,-1,0,1,-1,-1,1,2,3,4]
# # # ls= set(l)
# # # r = list(ls)
# # # r.sort()
# # # print(r)
# # # print(r[-1])

# # l = [-2,-77,74,0,7,18,18,33,74,34]
# # first = second = float('-inf')
# # for num in l:
# #     if num > first:
# #         third = second
# #         second = first 
# #         first = num
# #     elif num>second and num<first:
# #         third=second
# #         second = num
# #     elif num > third and num < second:
# #         third = num
# # print(first)
# # print(second)
# # print(third)

# c = 0 
# n = 6
# for i in range(1,n+1):
#     if n % i == 0:
#         c+=1
# if c ==2:
#             print("prime")
# else:
#             print("not prime")

l = [1,2,3,4,5]
# l.reverse()
# print(l)
# l[::-1]
# print(l)

rev= []
for num in l:
    rev = [num]+rev
print(rev)