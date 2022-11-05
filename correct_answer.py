# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if(n%2):
        print("Yes")
        for i in range(1,n//2+1):
            print(i,end=" ")
        for i in range(n,(n//2),-1):
            print(i,end=" ")
        print()
    elif(n!=2):
        print("Yes")
        print(n//2,end=" ")
        for i in range(1,n//2):
            print(i,end=" ")
        for i in range(n,n//2,-1):
            print(i,end=" ")
        print()
    else:
        print("No")