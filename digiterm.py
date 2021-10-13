for t in range(int(input())):
    n,d = map(int,input().split())
    temp = n
    rem,ans,c = 0,0,0
    while temp>0:
        rem = temp%10
        temp = temp//10
        c+=1
        if rem == d:
            temp = temp*pow(10,c)  + (rem+1)*pow(10,c-1)
            ans = temp - n
            c = 0
        
    print(ans)