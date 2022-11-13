# https://www.codechef.com/LRNDSA04/problems/ASHIGIFT
for _ in range(int(input())):
    x = int(input())
    list_b = list(map(int, input().split()))
    list_c = list(map(int, input().split()))

    bd, bp = [], []
    for i in range(1, len(list_b)):
        if i % 2 == 0:
            bp.append(list_b[i])
        else:
            bd.append(list_b[i])
    if len(list_c) > 1:
        res = 1
        cd, cp = [], []
        for i in range(1, len(list_c)):
            if i % 3 == 0:
                cp.append(list_c[i])
            elif i % 3 == 1:
                cd.append(list_c[i])
        j = 0
        for i in range(len(bd)):
            while j < len(cd) and cd[j] <= bd[i]:
                res -= cp[j]
                j += 1
            if j == len(cd):
                res += sum(bp[i:])
                break
            res += bp[i]

        if res > 0:
            print(res)
        else:
            print(1)

    else:
        print(sum(bp) + 1)
# end line
