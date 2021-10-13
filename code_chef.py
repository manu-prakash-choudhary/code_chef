for t in range(int(input())):
    n,k=map(int,input().split())
    strn = input().split()
    max1 = 0
    for i in range(n):
        max_length = 0
        unique=[]

        for j in range(i,n):
            if strn[j] in unique:
                max_length+=1
            else:
                unique.append(strn[j])
                if len(unique) == k:
                    max1 = max(max1,max_length)
                    break
                max_length+=1
        max1 = max(max1,max_length)
    print(max1)
