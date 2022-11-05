for _ in range(int(input())):
    k, q = map(int, input().split())
    sat = list(map(int, input().split()))
    mot = list(map(int, input().split()))
    q_list = []
    sum = []
    for i in sat:
        for j in mot:
            sum.append(i + j)
    sum.sort()
    for i in range(q):
        print(sum[int(input()) - 1] )
# this new line
