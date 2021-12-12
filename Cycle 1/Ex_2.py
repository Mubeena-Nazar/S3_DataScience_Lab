# Write Python program to create two matrices (read values from user) and  find the following

import numpy as np
a = []
r=int(input("Number of rows :: "))
print("Matrix :")
for x in range(r):
    a.append([int(y) for y in input().split()])
A = np.array(a)
print("\n\t\t")
print("Matrix :")
print("------------------------------------------")
print(A)


print("\n\t\t1.Dot Product")
print("------------------------------------------")
print("Matrix 2:")
a2 = []
for x in range(r):
    a2.append([int(y) for y in input().split()])
A2 = np.array(a2)
print("\nDot product:")
try:
    print(np.dot(A,A2))
except:
    print("OOP ! Shapes of metix are not aligned ")


print("\n\t\t2.Transpose :")
print("------------------------------------------")
print(A.transpose())


print("\n\t\t3.Trace:")
print("------------------------------------------")
print(A.trace())


print("\n\t\t4.Rank:")
print("------------------------------------------")
print(np.linalg.matrix_rank(A))


print("\n\t\t5.Determinant:")
print("------------------------------------------")
try:
    print(np.linalg.det(A))
except:
    print("Must be square matrix")
    
    
print("\n\t\t6.Inverse:")
print("------------------------------------------")
try:
    print(np.linalg.inv(A))
except:
    print("Must be square matrix")


print("\n\t\t7.Eigen Values and Vectors :")
print("------------------------------------------")
w, v = np.linalg.eig(A)
print("\nEigen Values : ")
print(w)
print("\nEigen vectors :")
print(v)
