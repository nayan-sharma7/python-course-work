import numpy as np
arr = np.array([1,2,3,4,5])
marks = [85,70,75,45,60]
# print(arr)

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2.ndim)

#no.of rows and column :-
print(arr.shape)
print(arr2.shape)

#no .of elements :- 
print(arr.size)
print(arr2.size)

#mathamtical 

#array operations with aggregate functions :-
arr = np.array([1,2,3,4,5])
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))  #average
print(np.sum(arr))