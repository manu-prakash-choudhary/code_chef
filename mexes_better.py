for t in range(int(input())):
    n,k = map(int,input().split())
    numbers_list = list(map(int,input().split()))
    mex_list = []
    def pairs(r = n,st=-1):
        if r == st:
            return
        for i in range(r-1,st,-1):
            temp = []
            for j in range(i,st,-1) :
                temp.append(numbers_list[j])
            mex_element(temp)
        pairs(r,st+1)
    def mex_element(temp):
        i = 0
        while i in temp:
            i+=1
        mex_list.append(i)
        return mex_list
    pairs(n)
    mex_list.sort()
    print(mex_list[k-1])
