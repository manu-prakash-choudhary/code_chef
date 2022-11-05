for _ in range(int(input())):
    s,x = map(int,input().split())
    strng = input()
    next_one = [None]*(s)

    #preprocessing of data
    count_zero = 0
    vac = 0
    vac_arr = [None]*s
    suf_vac_arr = [None]*(s)
    i=s-1
    pos1 = s
    while i>=0:
        next_one[i] = pos1
        if strng[i]=='0':
            count_zero+=1
        if count_zero==x:
            vac+=1
            count = 0
        if strng[i] == '1':
            count_zero = 0
            pos1 = i 

            
        suf_vac_arr[i] = vac
        i-=1
    ans = vac
    #now forward loop time
    i = 0
    count_zero = 0
    vac = 0
    while  i<s:
        if strng[i]=='1':
            if  next_one[i] > i + x - count_zero - 1:
                ans = max(ans,vac + suf_vac_arr[i-count_zero+x] + 1)
            count_zero = 0
        else:
            if count == x:
                vac+=1
                count = -1
            count+=1
        vac_arr[i] = vac
        i+=1
    # print(ans)

    print("next 1",next_one)
    print(suf_vac_arr)


