for _ in range(int(input())):
    k, q = map(int, input().split())
    sat = list(map(int, input().split()))
    mot = list(map(int, input().split()))
    q_list = []
    for i in range(q):
        temp = int(input())
        q_list.append(temp)
    sum = []
    for i in sat:
        for j in mot:
            sum.append(i + j)
    sum.sort()
    print(sum)
    for i in q_list:
        print(sum[i - 1])
# this new line
