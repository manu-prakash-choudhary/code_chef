import numpy as np
from numpy.core.defchararray import array
for t in range(int(input())):
    len_c = int(input())
    c_array = np.array(list(map(int,input().split())))

    n = int(input())
    n_array = np.array([])
    for i in range(n):
        n_array = np.append( n_array,np.array(list(map(int,input().split()))))
    n_array.reshape(n,n)
    
    sum_array = c_array[0] * np.identity(n)
    print("SUM_array", sum_array)
    n_array=n_array.reshape(n,n)
    print("n_array", n_array)
    print()

    print("c_array",c_array)
    matmul = n_array

    for i in range(1,len_c):
        sum_array +=  c_array[i]*matmul
        matmul = np.matmul(matmul,n_array)
        print(sum_array)
    if np.sum(sum_array) == 0:
        print('YES')
    else:
        print('NO')
    