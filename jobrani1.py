import numpy as np
mat=np.matrix([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
n=int(input("number="))
def function(mat,i):
    for j in range(1,i):
        mat*=mat
    return mat
result=np.matrix([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
for i in range(2,n+1):
    multiply=function(mat,i)
    result=result+multiply
print(result)
