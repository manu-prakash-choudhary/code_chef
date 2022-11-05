for _ in range(int(input())):
    n=int(input())
    char1 = 97
    str= ""
    if n==2:
        str += "ab"
        print(str)
        continue
    if n%2==0:
        keep = n//2
        i = 0
        while i<keep:
            str+=chr(char1)
            char1+=1
            i+=1
        while i >0:
            char1-=1
            str+=chr(char1)
            i-=1
    else:
        keep = (n+1)//2-1
        i = 0
        while i<keep:
            str+=chr(char1)
            char1+=1
            i+=1
        str+=chr(char1)
        while i >0:
            char1-=1
            str+=chr(char1)
            i-=1
            
    print(str)
