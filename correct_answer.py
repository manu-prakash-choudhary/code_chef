for __ in range(int(input())):
    N, K = map(int,input().split())
    L = list(map(int,input().split()))
    myDic = {i:0 for i in range(1,K+1)}
    colour = ans = j = 0
    for i in range(N):
        myDic[L[i]] += 1
        if myDic[L[i]] == 1:
            colour += 1
        while colour == K:
            myDic[L[j]] -= 1
            if myDic[L[j]] == 0:
                colour -= 1
            j += 1
        ans = max(i-j+1, ans)
    print(ans)