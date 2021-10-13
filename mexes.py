import numpy as np
import sys

for t in range(int(input())):
    n,k = map(int,input().split())
    def get_ints(): return np.array(list(map(int, sys.stdin.readline().strip().split())))
 
    numbers_list = get_ints()
    mex_list = np.array([],dtype=int)
    
    def pairs(r = n,st=-1):
        
        if r == st:
            return
        for i in range(r-1,st,-1):
            temp = np.array([],dtype=int)
            if st==-1:
                temp = np.append(temp,numbers_list[i::-1])
            else:
                temp = np.append(temp,numbers_list[i:st:-1])
            
            global mex_list
            i = 0
            while i in temp:
                i+=1
            mex_list = np.append(mex_list,i)
            
        pairs(r,st+1)
        
    
        
#__main__
    pairs(n)
    
    
    mex_list = np.sort(mex_list)
    print(mex_list[k-1])    


