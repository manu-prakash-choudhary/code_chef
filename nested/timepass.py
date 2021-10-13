# for t in range(int(input())):
#     m=int(input())
#     k=1
#     while k<m:
#         b=k
#         k=k*2
#     c=(m-b)+1

#     print(c)
for t in range(int(input())):
    n= int(input())
    k = 1
    while k<=n:
        k=k*2
    if n==k-1:
        print(k)
    else:
        print(k//2)


